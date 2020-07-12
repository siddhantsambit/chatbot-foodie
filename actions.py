from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib
import ssl
from flask_mail import Mail, Message
from email.message import EmailMessage

config = {"user_key": "85d488dec593c13117e68363869f2600"}
zomato = zomatopy.initialize_app(config)
email_data = []
sorted_list = []


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30, 'italian': 55, 'biryani': 7, 'north indian': 50,
                         'south indian': 85, 'mexican': 73, 'american': 1, 'thai': 95}
        results = zomato.restaurant_search(
            "", lat, lon, str(cuisines_dict.get(cuisine)), 100)
        d = json.loads(results)

        def sort(list):
            list.sort(key=lambda x: x[3], reverse=True)
            return list

        def enquiry(lis1):
            if len(lis1) == 0:
                return 0
            else:
                return 1

        response = ""
        global email_data
        global sorted_list
        if d['results_found'] == 0:
            response = "no results"
        else:
            if price == 'Lesser than Rs. 300':
                for i, restaurant in enumerate(d['restaurants']):
                    averageCostFor2 = restaurant['restaurant']['average_cost_for_two']
                    if averageCostFor2 <= 300:
                        name = restaurant['restaurant']['name']
                        address = restaurant['restaurant']['location']['address']
                        user_rating = restaurant['restaurant']['user_rating']['aggregate_rating']
                        send_list = [name, address, averageCostFor2, user_rating]
                        email_data.append(send_list)
                        if i == 9:
                            break

            elif price == 'Rs. 300 to 700':
                for i, restaurant in enumerate(d['restaurants']):
                    averageCostFor2 = restaurant['restaurant']['average_cost_for_two']
                    if averageCostFor2 >= 300 and averageCostFor2 <= 700:
                        name = restaurant['restaurant']['name']
                        address = restaurant['restaurant']['location']['address']
                        user_rating = restaurant['restaurant']['user_rating']['aggregate_rating']
                        send_list = [name, address, averageCostFor2, user_rating]
                        email_data.append(send_list)
                        if i == 9:
                            break

            elif price == 'More than 700':
                for i, restaurant in enumerate(d['restaurants']):
                    averageCostFor2 = restaurant['restaurant']['average_cost_for_two']
                    if averageCostFor2 >= 700:
                        name = restaurant['restaurant']['name']
                        address = restaurant['restaurant']['location']['address']
                        user_rating = restaurant['restaurant']['user_rating']['aggregate_rating']
                        send_list = [name, address, averageCostFor2, user_rating]
                        print(send_list)
                        email_data.append(send_list)
                        if i == 9:
                            break
        print(email_data)
        sorted_list = sort(email_data)

        if (enquiry(sorted_list) == 0):
            dispatcher.utter_message("No results found!!!")

        else:
            for i, detail in enumerate(sorted_list):
                j = i
                response = str(j + 1) + ". " + detail[0] + " in " + \
                           detail[1] + " has been rated " + detail[3] + "\n"
                dispatcher.utter_message(response)
                if i == 4:
                    break

        return []


class ActionSendEmail(Action):
    def __init__(self):
        pass

    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('emailid')
        # Get location and cuisines
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        # global d_email_rest
        len_list = len(sorted_list)
        if len_list < 10:
            email_rest_count = len(sorted_list)
        else:
            email_rest_count = 10
        d_email_subj = "Top " + str(email_rest_count) + " " + cuisine + " restaurants in " + str(loc)
        d_email_msg = "Hi there!!! Here are the " + d_email_subj + "." + "\n"
        for i, restaurant in enumerate(sorted_list):
            j = i
            d_email_msg = d_email_msg + str(j + 1) + ". " +restaurant[0] + " in " + restaurant[1] + " has been rated " + restaurant[3] + "\n"
            if i == (email_rest_count - 1):
                break

        s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        # s.starttls()
        s.login("foodieupgradchatbot@gmail.com", "foodie1234")
        msg = EmailMessage()
        msg['Subject'] = d_email_subj
        msg['From'] = "foodieupgradchatbot@gmail.com"
        msg.set_content(d_email_msg)
        msg['To'] = to_email
        s.send_message(msg)
        s.quit()
        dispatcher.utter_message("**** Email Sent to " + to_email + " ! HAPPY DINING :) ****")
        return []


class VerifyLocation(Action):
    def name(self):
        return 'action_verify_location'

    TIER_1 = []
    TIER_2 = []

    def __init__(self):
        self.TIER_1 = ['ahmedabad', 'bangalore', 'chennai',
                       'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune']
        self.TIER_2 = ['agra', 'ajmer', 'aligarh', 'allahabad', 'amravati', 'amritsar', 'asansol', 'aurangabad',
                       'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner',
                       'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad',
                       'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur',
                       'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 'hubli-dharwad', 'indore', 'jabalpur',
                       'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kannur',
                       'kanpur', 'kakinada', 'kochi',
                       'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'lucknow', 'ludhiana',
                       'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore',
                       'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 'pondicherry', 'raipur',
                       'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur',
                       'srinagar', 'sultanpur', 'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli',
                       'tirunelveli', 'tiruppur', 'ujjain', 'vijayapura', 'vadodara', 'varanasi', 'vasai-virar city',
                       'vijayawada', 'visakhapatnam', 'warangal']

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        print(loc)
        if not (self.verify_location(loc)):
            dispatcher.utter_message(
                "We do not operate in that area yet. Please try some other city.")
            print('inside no')
            return [SlotSet('location', None)]
        else:
            dispatcher.utter_message(
                "Great we serve in " + loc + ".")
            return [SlotSet('location', loc)]

    def verify_location(self, loc):
        if loc is None:
            return False
        return loc.lower() in self.TIER_1 or loc.lower() in self.TIER_2
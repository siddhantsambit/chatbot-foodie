from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import send_mail

config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
zomato = zomatopy.initialize_app(config)

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85,'mexican':73,'american':1}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			if price =='Lesser than Rs. 300':
        		for i,restaurant in enumerate(d['restaurants']):
                    averageCostFor2 = restaurant['restaurant']['average_cost_for_two']
                    if averageCostFor2 <= 300:
                        name = restaurant['restaurant']['name']
                        address = restaurant['restaurant']['location']['address']
                        user_rating = restaurant['restaurant']['user_rating']['aggregate_rating']

                        send_list = [name,address,averageCostFor2,user_rating]
                        email_data.append(send_list)

            elif price =='Rs. 300 to 700':
                for i,restaurant in enumerate(d['restaurants']):
                    averageCostFor2 = restaurant['restaurant']['average_cost_for_two']
                    if averageCostFor2 >= 300 and averageCostFor2 <= 700:
                        name = restaurant['restaurant']['name']
                        address = restaurant['restaurant']['location']['address']
                        user_rating = restaurant['restaurant']['user_rating']['aggregate_rating']

                        send_list = [name,address,averageCostFor2,user_rating]
                        email_data.append(send_list)
            elif price =='More than 700':
                for i,restaurant in enumerate(d['restaurants']):
                    averageCostFor2 = restaurant['restaurant']['average_cost_for_two']
                    if averageCostFor2 >= 700:
                        name = restaurant['restaurant']['name']
                        address = restaurant['restaurant']['location']['address']
                        user_rating = restaurant['restaurant']['user_rating']['aggregate_rating']

                        send_list = [name,address,averageCostFor2,user_rating]
                        email_data.append(send_list)
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

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
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        else:
            dispatcher.utter_message(
                "Great we serve in " + loc + ".")
            return [SlotSet('location', loc), SlotSet("location_ok", True)]

    def verify_location(self, loc):
        return loc.lower() in self.TIER_1 or loc.lower() in self.TIER_2


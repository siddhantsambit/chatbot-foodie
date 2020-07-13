## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## price specified
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_price
* restaurant_search{"price":"Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email":"Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid":"siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email
* goodbye
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_verify_location
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* affirm{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - utter_ask_location
* affirm{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_verify_location
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "tinaghosh1990@gmail.com"}
    - slot{"emailid": "tinaghosh1990@gmail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "tinaghosh1990@gmail.com"}
    - slot{"emailid": "tinaghosh1990@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chandigarh"}
    - action_verify_location
    - slot{"location": "Chandigarh"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* stop
    - utter_default
    - utter_ask_howcanhelp
* restaurant_search{"cuisine": "cafe", "location": "Kolkata"}
    - slot{"cuisine": "cafe"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - utter_ask_email
    - utter_ask_email
* restaurant_search
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "bhadrak"}
    - slot{"location": "bhadrak"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - action_verify_location
    - slot{"location": "cuttack"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "soumyamoharana1992@gmail.com"}
    - slot{"emailid": "soumyamoharana1992@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bongaon"}
    - slot{"location": "bongaon"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Azamgarh"}
    - slot{"location": "Azamgarh"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "Siliguri"}
    - slot{"location": "Siliguri"}
    - action_verify_location
    - slot{"location": "Siliguri"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "tinaghosh1990@gmail.com"}
    - slot{"emailid": "tinaghosh1990@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Balasore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Balasore"}
    - action_verify_location
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Nepal"}
    - slot{"location": "Nepal"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_verify_location
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "biryani", "location": "Nagpur"}
    - slot{"cuisine": "biryani"}
    - slot{"location": "Nagpur"}
    - action_verify_location
    - slot{"location": "Nagpur"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "biryani", "location": "Hyderabad"}
    - slot{"cuisine": "biryani"}
    - slot{"location": "Hyderabad"}
    - action_verify_location
    - slot{"location": "Hyderabad"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Singur"}
    - slot{"location": "Singur"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - action_verify_location
    - slot{"location": "Coimbatore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "tinaghosh1990@gmail.com"}
    - slot{"emailid": "tinaghosh1990@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "cafe", "location": "Lucknow"}
    - slot{"cuisine": "cafe"}
    - slot{"location": "Lucknow"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "tinaghosh1990@gmail.com"}
    - slot{"emailid": "tinaghosh1990@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "cafe", "location": "Goa"}
    - slot{"cuisine": "cafe"}
    - slot{"location": "Goa"}
    - action_verify_location
    - slot{"location": "Goa"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "tinaghosh1990@gmail.com"}
    - slot{"emailid": "tinaghosh1990@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "bakery", "location": "bangalore"}
    - slot{"cuisine": "bakery"}
    - slot{"location": "bangalore"}
    - action_verify_location
    - slot{"location": "bangalore"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Send Mail"}
    - slot{"email": "Send Mail"}
    - utter_ask_emailid
* restaurant_search{"emailid": "siddhantsambit@gmail.com"}
    - slot{"emailid": "siddhantsambit@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye

# interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_verify_location
    - slot{"location": "Amritsar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
* affirm
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - action_verify_location
    - slot{"location": "kochi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Jaipur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Jaipur"}
    - action_verify_location
    - slot{"location": "Jaipur"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_verify_location
    - slot{"location": "Agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "jalandhar"}
    - slot{"location": "jalandhar"}
    - action_verify_location
    - slot{"location": "jalandhar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_verify_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - utter_ask_email
* restaurant_search{"email": "Dont Send Email"}
    - slot{"email": "Dont Send Email"}
    - utter_goodbye
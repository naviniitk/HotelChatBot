# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# # class ActionHelloWorld(Action):

# #     def name(self) -> Text:
# #         return "action_hello_world"

# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# #         dispatcher.utter_message(text="Hello World!")

# #         return [] 


class BookRoomForm(FormAction):
 def name(self):
  return "book_room_form"

 def required_slots(self,tracker) -> List[Text]:
  return ["no_of_rooms", "type_of_room"]

 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    return {
            "no_of_rooms": [
                self.from_text(),
            ],
            "type_of_room": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_message("Your booking details are here")    
    return []

class BookRoomsDetails(FormAction):

    def name(self):
        return "action_book_rooms_details"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        rooms = tracker.get_slot("no_of_rooms")
        room_type = tracker.get_slot("type_of_room")
        dispatcher.utter_message(text="You have chosen {} {} rooms".format(rooms, room_type))

        return []

# class ActionCleanRoom(Action):
#     def name(self):
#         return "action_clean_room"
    
    
#     def submit(self, dispatcher: CollectingDispatcher,
#                tracker: Tracker,
#                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Sure, I will send someone to your room right away")
        
#         return []
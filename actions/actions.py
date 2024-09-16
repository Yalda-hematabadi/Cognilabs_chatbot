from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from openai import OpenAI

class ActionGetOpenAIResponse(Action):
    def name(self) -> Text:
        return "action_get_openai_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_query = tracker.latest_message.get('text')
        legal_topics = [
            "contract law", "privacy law", "corporate legal matters", "labor law", 
            "intellectual property", "regulatory consulting", "legal advisory", 
            "legal consulting", "civil law", "legislation", "lawful"
        ]

        if any(topic in user_query.lower() for topic in legal_topics):
            response = self.get_openai_response(user_query)
            response += "\n\nPlease note: This information is for general guidance only and does not constitute legal advice."
            dispatcher.utter_message(text=response)
        else:
            dispatcher.utter_message(text="I can only assist with questions related to contract law, privacy law, corporate legal matters, labor law, and intellectual property. Please rephrase your question.")

        return []

    def get_openai_response(self, prompt: str) -> str:
        client = OpenAI(api_key='sk-5LjOBi4FDJu-MKQ7uzfif5Af1X6ve0waFv-ruBTqmqT3BlbkFJNVf6HWf39spOIQCtUyQlpSxGO-I0AFj5WkGogmZXkA')
        
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a legal assistant specializing in law-related matters. Provide concise and informative responses."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message['content']

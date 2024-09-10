# Congnilabs_chatbot

# Legal Assistant Chatbot

This project implements a chatbot designed to assist users with legal queries using Rasa and OpenAI's GPT-4 model.

## Features

- Handles user queries related to various legal topics including contract law, privacy law, corporate legal matters, labor law, and intellectual property.
- Utilizes OpenAI's GPT-4 model to generate informative responses to legal questions.
- Implements a conversational flow to clarify user queries and provide more detailed information when needed.

## Setup

1. Create a virtual machine 

2. Install the required dependencies:
   ```
   pip install rasa[full] openai
   ```

3. Train the Rasa model:
   ```
   rasa train
   ```

4. Run the actions server:
   ```
   rasa run actions
   ```

5. In a separate terminal, run the rasa shell:
   ```
   rasa shell
   ```

## Project Structure

- `domain.yml`: Defines the chatbot's domain, including intents, entities, slots, and actions.
- `config.yml`: Configuration file for Rasa NLU and Core models.
- `data/nlu.yml`: Training data for natural language understanding.
- `data/stories.yml`: Conversation flow definitions.
- `data/rules.yml`: Defines rules for specific conversation patterns.
- `actions.py`: Custom actions, including the integration with OpenAI's API.

## Custom Action: ActionGetOpenAIResponse

This action is triggered when a user asks a legal question. It performs the following steps:

1. Checks if the user's query is related to the supported legal topics.
2. If relevant, sends the query to OpenAI's GPT-4 model to generate a response.
3. Appends a disclaimer to the response.
4. If the query is not related to supported topics, it prompts the user to rephrase their question.

## Important Note

This chatbot provides general guidance only and does not constitute legal advice. Users should be advised to consult with a qualified legal professional for specific legal issues.
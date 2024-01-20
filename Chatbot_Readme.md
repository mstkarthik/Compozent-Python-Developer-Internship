**Simple Chatbot with Question-Answer Functionality**
Welcome to the Simple Chatbot with Question-Answer Functionality! This Python script allows you to interact with a basic chatbot capable of answering questions and learning new responses. The chatbot uses a predefined set of questions and answers but can also adapt and learn from user input.

**Features**
Question-Answer Knowledge Base: The chatbot loads a JSON file containing a list of predefined questions and their corresponding answers.
Intelligent Matching: Utilizes the difflib library to find the best match for user input, allowing flexibility in question phrasing.
Learning Capability: If the chatbot doesn't know the answer to a user's question, it asks for input and learns from the user's response, appending the new question-answer pair to its knowledge base.
**How to Use**
Run the Script:

Execute the script in a Python environment.
Ensure the json and difflib modules are installed.
Interaction:

Enter your questions or statements when prompted by the chatbot.
Type "quit" to exit the chatbot.

**Learning:**

If the chatbot doesn't know the answer, it will ask for input.
Type the answer or "skip" to move on to the next question.
Knowledge Base:

The chatbot's knowledge base is stored in a JSON file (QA.json).
You can manually edit this file to add or modify questions and answers.
Example Knowledge Base
json
{
  "questions": [
    {
      "question": "What's your favorite color?",
      "answers": ["I don't have a favorite color, but I like all the colors!", "I'm a chatbot, so I don't have preferences, but I think blue is nice."]
    },
    // ... other questions and answers ...
  ]
}

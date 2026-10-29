# FlatMate Food

## Project overview

FlatMate Food is a Streamlit application designed to reduce food waste in shared kitchens. Users can manage their kitchen stock, generate AI-powered recipe suggestions, and identify missing ingredients for predefined recipes.

## Technologies used

- Python
- Streamlit
- Groq API
- GPT-OSS 20B (`openai/gpt-oss-20b`)
- OpenAI Python SDK, configured to communicate with the Groq API

## Installation

1. Install Python.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Install the dependencies:

   `pip install -r requirements.txt`

## Configuration

Create or obtain a Groq API key. Configure it as `GROQ_API_KEY` in your environment or in the Streamlit secrets settings.

Never publish your API key in the repository.

## Run the application

Run the following command from the project folder:

`streamlit run app.py`

## Main features

- Add ingredients to a shared kitchen stock.
- Select available cooking equipment.
- Generate recipe suggestions using a large language model through the Groq API.
- Browse predefined recipes.
- Generate a shopping list based on missing ingredients.

## Data and reproducibility

The application uses Python-defined recipe data and user-entered kitchen stock, as implemented in the source code. AI-generated suggestions require a valid Groq API key and an available API service. The generated suggestions may vary between requests.

## AI usage and references

The application uses the Groq API to access the configured GPT-OSS 20B model. The OpenAI Python SDK is used as the API client.

Include the official documentation links, package versions where relevant, and the prompts used during development and AI recipe generation in the supporting documentation.

## Limitations

AI-generated recipes are guided by instructions in the prompt, but their compatibility with all constraints is not formally guaranteed. Ingredient quantities are not fully accounted for by the shopping-list logic.

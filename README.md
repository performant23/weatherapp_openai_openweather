# weatherbot_openai_openweather

The Weather Chatbot is a Python-based command-line application that responds with weather information or answers general questions. It integrates the OpenWeather API for fetching weather data and the OpenAI language model (gpt 3.5 turbo) for generating responses.

## Features

- Provides weather information for specified locations.
- Generates appropriate responses for general questions using the OpenAI language model.
- Handles error cases, such as invalid prompts or failed API requests, with suitable error messages.

## Requirements
1. Python 3.7.1+
2. API keys for OpenWeather and OpenAI.

## Weather-related Prompts
If your prompt is weather-related (e.g., "Tell me the weather in Mumbai" or "How is the weather today in Mumbai"), the chatbot will call the OpenWeather API to fetch weather data for the specified location and provide a response.

## General Questions
For non-weather prompts (e.g., "Who is the President of the United States"), the chatbot will utilize the OpenAI language model to generate appropriate responses.

## Error Handling
The chatbot includes error handling mechanisms for the following scenarios:
- Failed API requests: If there is an issue with the OpenWeather API or OpenAI API, the chatbot will display an error message indicating the failure.
- Invalid prompts: If the chatbot cannot detect the location in a weather-related prompt, it will display a message stating that the location couldn't be detected.

import openai
import requests
import json

openai.api_key = 'xxxxxxxxxxxxxxxxxxx'
weather_api_key = 'xxxxxxxxxxxxxxx'
    

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
    else:
        return "Failed to fetch weather information."


def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()
    except openai.error.APIError as e:
        return f"Error: {e.message}"

def chatbot():
    while True:
        user_input = input("Enter Prompt (or press 0 to abort): ")
        if user_input == "0":
            break
        response = generate_response(user_input + "Is the previous statment about weather-related aspects (reply with yes/no)?")
        is_weather_related = response.lower().startswith("yes")
        if is_weather_related:
            location = generate_response(user_input + "Detect only the location in the previous sentence (don't respond with anything else, just the location), if the sentence contains any place smaller than a city, detect its city and respond with just the city name")
            print(location)
            if location:
                weather_response = fetch_weather(location)
                if weather_response == "Failed to fetch weather information.":
                    print("Chatbot: Error occurred while fetching weather information.")
                else:
                    print("Chatbot:", weather_response)
            else:
                print("Chatbot: Sorry, I couldn't detect the location in the query.")
        else:
            response = generate_response(user_input)
            print("Chatbot:", response)



if __name__ == "__main__":
    chatbot()

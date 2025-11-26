# dihctionaries
from pyscript import display

weather_today = {
    'location' : 'Manila',   # where the weather is 
    'temperature_c' : 32,    # current temperature in Celsius
    'humidity' : 78,     # current humidity percentage
    'condition' : 'Sunny'     # current weather condition
}

weather_today['condition'] = 'Cloudy'     # update condition
weather_today['heat_index'] = 38    # calculated heat index its slightly higher than base body temperate so we would perceieve it as hot at 38 its already dangerous for humans to be outside for long periods of time
display(weather_today, target="output")


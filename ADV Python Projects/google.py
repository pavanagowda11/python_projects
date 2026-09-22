import json
import webbrowser

# Get input from user
source = input("Enter source: ")
destination = input("Enter destination: ")

# Store source and destination in JSON
data = {
    "source": source,
    "destination": destination
}

# Display JSON
print("\nJSON Data:")
print(json.dumps(data, indent=4))

# Create Google Maps URL
url = f"https://www.google.com/maps/dir/{source.replace(' ', '+')}/{destination.replace(' ', '+')}"

# Open Google Maps
webbrowser.open(url)

print("\nOpening Google Maps...")
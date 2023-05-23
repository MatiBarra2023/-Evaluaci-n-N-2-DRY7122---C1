import urllib.parse
import requests
import json

main_api = "https://www.mapquestapi.com/directions/v2/route?"
origin = "Santiago"
dest = "Temuco"
key = "SiWmyszv8znGG67FYHjXdjO9yTs14b7E"
url = main_api + urllib.parse.urlencode({"key":key,"from":origin,"to":dest})

json_data = requests.get(url).json()
print(json_data)

print(" ")

#print("API Status: " + str(json_data) + " = A successful route call.\n") 
print("=============================================")
print("Directions from " + (origin) + " to " + (dest))
print("Trip Duration:	" + (json_data["route"]["formattedTime"])) 
print("Miles:	" + str(json_data["route"]["distance"]))
#print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
print("=============================================")

#print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
#print("=============================================")
for each in json_data["route"]["legs"][0]["maneuvers"]:
    print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
print("=============================================\n")


print(" ")
print("Finish")
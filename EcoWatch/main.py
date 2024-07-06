"""
this program is a weather app that gets weather status from a remote api
"""
import geocoder as ge
import json
import socket
# import request



class EcoWatch:

    def getMyLocation(self): #to get my computer current ip address

        try:
            data = socket.socket()
            name = socket.gethostbyname("localhost")
        except Exception: f"failed to get host address"


        try:  #getting host address with geocoder
            ip_address = ge.ip(name)
        except Exception:  f"could not get location"

        try:
            myLocation = ge.ipinfo(ip_address)
        except Exception: f"could not load ip address"

        try:
            with open("myaddress.json", mode="w") as address:
                json.dump(myLocation, address)
        except Exception: f"failed to create json file"

        try:
            with open("myaddress.json", mode= "r") as data:
                my_data = dict(json.load(data))
        except Exception: f"could not load data from json"

        return my_data



    def __init__(self):
        self.data = self.getMyLocation()



    def myLocation(self):

        self.country = country
        self.state = state
        self.city = city
        self.loc = loc
        
        country = self.getMyLocation(["country"])
        state = self.getMyLocation(["region"])
        city = self.getMyLocation(["city"])
        loc = self.getMyLocation(["loc"])

    def getWeather(self):
        pass



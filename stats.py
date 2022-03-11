# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:55:06 2022

@author: jakob
"""

from pymongo import MongoClient


cluster = "mongodb+srv://Jakob:qazwerty@cluster0.0o0mq.mongodb.net/matchStats?retryWrites=true&w=majority"
client = MongoClient(cluster)

print (client.list_database_names())

db = client.matchStats

print(db.list_collection_names())


moba = db.moba
moba.clear


match1 = {"Gamertag": "Noobkiller", "Heroname": "Medusa", "Kills": "13", "Deaths":"8", "Result":"Win"}
match2 = {"Gamertag": "Noobkiller", "Heroname": "Pyromancer", "Kills": "1", "Deaths":"12", "Result":"Loss"}
match3 = {"Gamertag": "Noobkiller", "Heroname": "Pebbels", "Kills": "22", "Deaths":"2", "Result":"Win"}
match4 = {"Gamertag": "Noobkiller", "Heroname": "Medusa", "Kills": "5", "Deaths":"8", "Result":"Loss"}
match5 = {"Gamertag": "Noobkiller", "Heroname": "Myrmidon", "Kills": "2", "Deaths":"4", "Result":"Win"}
match6 = {"Gamertag": "Noobkiller", "Heroname": "Slither", "Kills": "4", "Deaths":"3", "Result":"Loss"}
match7 = {"Gamertag": "Noobkiller", "Heroname": "Bubbles", "Kills": "7", "Deaths":"6", "Result":"Win"}
match8 = {"Gamertag": "Noobkiller", "Heroname": "Bubbles", "Kills": "6", "Deaths":"2", "Result":"Win"}
match9 = {"Gamertag": "Noobkiller", "Heroname": "Bubbles", "Kills": "4", "Deaths":"6", "Result":"Loss"}
match10 = {"Gamertag": "Noobkiller", "Heroname": "Aracna", "Kills": "4", "Deaths":"5", "Result":"Win"}

"""
moba.insert_one(match1)
moba.insert_one(match2)
moba.insert_one(match3)
moba.insert_one(match4)
moba.insert_one(match5)
moba.insert_one(match6)
moba.insert_one(match7)
moba.insert_one(match8)
moba.insert_one(match9)
moba.insert_one(match10)
"""


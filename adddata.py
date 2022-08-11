import requests
import time
import pymongo


client = pymongo.MongoClient("mongodb://Pinkesh:Pinke$h911@cluster01-shard-00-00.ao46i.mongodb.net:27017,cluster01-shard-00-01.ao46i.mongodb.net:27017,cluster01-shard-00-02.ao46i.mongodb.net:27017/?ssl=true&replicaSet=atlas-gc9g1d-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["cryptodb"]
coll = db["crypto"]


while True:
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    currencies = ["LTCUSDT","ETHUSDT","BNBUSDT","NEOUSDT","MCOUSDT","BCCUSDT"]

    data = {}
    for i in currencies:
        url = key + i
        r = requests.get(url)
        d = r.json()
        
        data[d['symbol']] = d['price']
    
    print(data)
    
    coll.insert_one(data)
    time.sleep(10)
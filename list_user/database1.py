import pymongo
import json

def db_all(users):
    db_list = []
    for x in mycol.find():
        data = str(x).replace("ObjectID(","")
        data = data.replace(")","")
        data = data.replace("","")
        data = data.replace('"data":"{','')
        data = data.replace('}"','')
        db_list.append(json.loads(data))
    return db_list

def main(host_ip):
    db_add = "mongodb2://192.168.35.128:27018/"
    myclient = pymongo.MongoClient(db_add)
    mydb = myclient["mydatabase"]
    mycol = mydb["key"]
    return db_all(users)

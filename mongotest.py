import pymongo
client = pymongo.MongoClient("mongodb+srv://suman:suman123@cluster0.suttp1v.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={"name":"suman","mail":"sumanvh007@gmail.com","surname":"vh"}
db1=client["mangotest"]
coll=db1.test
coll.insert_one(d)
gnsgakmgfl;a,
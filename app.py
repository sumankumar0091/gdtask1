from flask import Flask,request, json, Response, jsonify
from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client.greendeckdb
collection=db.greendeck

greendeck = Flask(__name__)

@greendeck.route('/api/greendeck',methods=['GET']) 
def read_record():
    qry = request.args.get('qry')
    
    result=collection.find_one({"name": qry})
    
    if result==None:
        return Response(response="Value Not Found!")
    else:
        result.pop('_id', None)
        return jsonify(result)



@greendeck.route('/api/greendeck',methods=['POST'])    
def insert_record():
    data = request.get_json()

    result=collection.insert_one(data)

    if result==None:
        return Response(response="No Value Inserted!")
    else:
        return jsonify("record inserted successfully")


@greendeck.route('/api/greendeck',methods=['PUT'])
def update_redord():
    data = request.get_json()
    qry = request.args.get('name')

    result=collection.update_one({"name":qry},{ "$set": data })

    if result==None:
        return Response(response="No Value Inserted!")
    else:
        return jsonify("record updated successfully")


@greendeck.route('/api/greendeck',methods=['DELETE'])
def delete_record():
    qry = request.args.get('qry')
    result=collection.delete_one({"name": qry})
    
    if result==None:
        return Response(response="No Value Inserted!")
    else:
        return jsonify("record deleted successfully")
 
if __name__ == '__main__':
    greendeck.run(debug=True, port=5000, host='0.0.0.0')


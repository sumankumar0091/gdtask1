# Project Description

Create a REST API using Python and host it locally using Docker.
Implementing the concept of APIs and Containerization. Record of 5000 products in JSON format was dumped. These products are sold on their E-Commerce platform. The data contains the product name, price and other information. The purpose is to allow the user to interact with a database of products using APIs which are available on localhost via Docker.

# Links
GitHub: https://github.com/sumankumar0091/gdtask1


# Installation and Quickstart
### Install MongoDB on host
Install MongoDB on Ubuntu using guidelines mentioned in https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04

### Ingest Data into MongoDB
After installation, to create a database in mongodb, first login to mongodb usign the mongo client. To create a database use the following command
```
use greendeckdb
```
Create collection in mongodb as
```
db.createCollection("greendeck")
```

To ingest the data, first download the CSV data given in the assignment. To ingest the CSV data directly into mongodb use the following command
```
mongoimport --type csv -d greendeckdb -c greendeck --headerline --drop Greendeck\ SE\ Assignment\ Task\ 1.csv
```

### Build and Deploy API Server using Docker
After cloning the git repo
```
cd gdtask1
```
Build the Docker Image from the given Dockerfile as follows
```
docker build -t gd_api_server .
```
After the docker Image is built, the next step would be to start the container. Because we are running MongoDB on host (not containerized), it is necessary to start docker container on host's network. To enable this, we use **--network=host** flag while starting the container. 

```
docker run --network=host gd_api_server
```
The api server is configured to run at http://localhost:5000
 
# Accessing the APIs
Attaching sample CURL requests for all CRUD Operations
## GET
```
curl -X GET -H "Content-Type: application/json"  http://localhost:5000/api/greendeck?qry=JUNAROSE%20Curve%20Mulle%20Toile%20Print%20Top%20%20Vanilla%20Ice
```
## POST
```
curl -X POST -d  '{  "brand_name": "NEWLY INSERTED RECORD",   "classification_l1": "men",   "classification_l2": "women umbrellas",   "classification_l3": "",   "classification_l4": "",   "currency": "GBP", "name": "NEWLY INSERTED RECORD",   "offer_price_value": 8,   "regular_price_value": 8}' -H 'Content-Type:application/json' http://localhost:5000/api/greendeck
```

## PUT
```
curl -X PUT -H "Content-Type: application/json" -d '{"name" : "hush Gabby Weekend Leather Bag  Black", "regular_price_value" : 249, "offer_price_value" : 249, "currency" : "GBP", "offer_price_value": 100 }'  http://localhost:5000/api/greendeck?qry=hush%20Gabby%20Weekend%20Leather%20Bag%20%20Black
```
## DELETE
```
curl -X DELETE -H "Content-Type: application/json"  http://localhost:5000/api/greendeck?qry=Oasis%20Broderie%20Short%20Sleeve%20Top%20%20Black
```
### See also
https://towardsdatascience.com/how-to-deploy-a-mongodb-replica-set-using-docker-6d0b9ac00e49
https://medium.com/@pierangelo1982/mongodb-with-docker-7eeb02f4d667

### License
This package is distributed under the **[MIT license](https://opensource.org/licenses/MIT).**
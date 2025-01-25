# from motor.motor_asyncio import AsyncIOMotorClient
# from odmantic import AIOEngine
from os import getenv

from mongoengine import connect
import pymongo
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from config import backend_ip

print(f'Starting Engine in {getenv("ENVIRONMENT")}')

MONGO_DATABASE_URL = f"mongodb+srv://anidl:encodes@cluster0.oobfx33.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" \
    if getenv('ENVIRONMENT') == 'dev' else \
    "mongodb://user:password@localhost:27017/"
MONGO_DATABASE = "shop"

# client = AsyncIOMotorClient(MONGO_DATABASE_URL)
# print('Engine Started')
# engine = AIOEngine(motor_client=client, database=MONGO_DATABASE)
mongo_client = MongoClient(MONGO_DATABASE_URL)
db = mongo_client.shop

# Base.metadata.create_all(bind=eng)

# metadata = MetaData()

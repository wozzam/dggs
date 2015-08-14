'''
Created on 14 Aug 2015

@author: admin
'''
#notes
#need to import src and dlls from the DGGSPython27 folder into the new project

#database imports
import psycopg2
from pymongo import MongoClient
import time

#dggs imports
from src.uk.co.riskaware.dggs.enums.shape_string_format import ShapeStringFormat
from src.uk.co.riskaware.dggs.dggs import Dggs
from src.uk.co.riskaware.dggs.enums.model import Model
from src.uk.co.riskaware.dggs.shapes.dggs_cell import DggsCell
from src.uk.co.riskaware.dggs.shapes.dggs_linestring import DggsLinestring
from src.uk.co.riskaware.dggs.shapes.dggs_polygon import DggsPolygon
from src.uk.co.riskaware.dggs.enums.shape_string_format import ShapeStringFormat

#mongo set up
client = MongoClient('localhost', 27017)
db = client.dggs
collection = db.twitter_dggs_3h

#postgres set up
dbname = "uk_tweets"
user = "postgres"
password = "postgres"
host = "localhost"
sql_query = "select lat, lon from tweets limit 10;" #this takes about 17 seconds for 1 million, change limit as needed

connection = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)

cursor = connection.cursor()
start_time = time.time()
cursor.execute(sql_query)
result = cursor.fetchall()

for row in result:
    lat = str(row[0])
    lon = str(row[1])
    wkt_string = 'GEOMETRYCOLLECTION(''POINT('+lon+' '+lat+'))'
    
    # Convert the shape string
    dggs = Dggs(Model.ISEA3H) # change  between this and ISEA4T
    dggs_shapes = dggs.convert_shape_string_to_dggs_shapes(wkt_string, ShapeStringFormat.WKT, 1.234)
    
    for item in dggs_shapes:
        dggs_cellID = item.get_shape().get_cell_id()
        mongo_insert = {"lon": lon, "lat": lat, "cell_id": dggs_cellID}
        collection.insert(mongo_insert)
        
end_time = time.time() - start_time
print end_time
    

    
'''
Created on 13 Aug 2015

@author: admin
'''
from src.uk.co.riskaware.dggs.enums.shape_string_format import ShapeStringFormat
from src.uk.co.riskaware.dggs.dggs import Dggs
from src.uk.co.riskaware.dggs.enums.model import Model
from src.uk.co.riskaware.dggs.shapes.dggs_cell import DggsCell
from src.uk.co.riskaware.dggs.shapes.dggs_linestring import DggsLinestring
from src.uk.co.riskaware.dggs.shapes.dggs_polygon import DggsPolygon
from src.uk.co.riskaware.dggs.enums.shape_string_format import ShapeStringFormat

#create dggs cells from wkt

wkt_string = ('GEOMETRYCOLLECTION('
                      'POINT(2.345 1.234))'
                      )
# Convert the shape string
dggs = Dggs(Model.ISEA4T) # change  between these two fro hex and tri
#dggs = Dggs(Model.ISEA3H)
dggs_shapes = dggs.convert_shape_string_to_dggs_shapes(wkt_string, ShapeStringFormat.WKT, 3.884)
dggs_cells_list = []

for item in dggs_shapes:
    x = item.get_shape()
    print x
    y = item.get_shape().get_cell_id()
    print y
    dggs_cells_list.append(item.get_shape())

#create kml file
kml_filename = "5_ActualKmlFile.kml"    
dggs.create_dggs_kml_file(kml_filename, dggs_cells_list) # dggs_cells_list is list of the get shape objects

#create kml from dggs cell

#dggs_cells = [DggsCell("072311311111"), DggsCell("0701200000130")]
# Create a KML file for the DGGS cells
#dggs = Dggs(Model.ISEA4T)
# kml_filename = "3_ActualKmlFile.kml"
# dggs.create_dggs_kml_file(kml_filename, dggs_cells)

#dggs to wkt

shape_stringwkt = dggs.convert_dggs_cells_to_shape_string(dggs_cells_list, ShapeStringFormat.WKT)
shape_stringgeojson = dggs.convert_dggs_cells_to_shape_string(dggs_cells_list, ShapeStringFormat.GEO_JSON)

print shape_stringwkt
print shape_stringgeojson



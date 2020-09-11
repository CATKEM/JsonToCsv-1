import json
import csv

with open('data.json') as json_file: 
    json_data = json.load(json_file)

for worksheet in json_data:
    out_file = open(worksheet+'.csv', 'w')
    csv_writer = csv.writer(out_file)
    headers_written = False
    
    for stock_data in json_data[worksheet]:
        if not headers_written:
            headers = stock_data.keys()
            csv_writer.writerow(headers)
            headers_written = True
        csv_writer.writerow(stock_data.values())

    out_file.close()

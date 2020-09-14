import json
import csv

with open('data.json') as json_file: 
    json_data = json.load(json_file)

bdrId = json_data["classifications"][0]["bdrId"]
classifications = json_data["classifications"][0]["classifications"]

for worksheet in json_data:
    out_file = open(bdrId+'.csv', 'w', newline='\n', encoding='utf-8')
    csv_writer = csv.writer(out_file)
    headers_written = False
    
    for classification in classifications:
        if not headers_written:
            headers = classification.keys()
            csv_writer.writerow(headers)
            headers_written = True
        csv_writer.writerow(classification.values())

    out_file.close()

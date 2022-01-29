import csv
import json

src = 'coincodex/daily/20220128.json'
dest = 'coincodex/daily/20220128.csv'

with open(src, 'r', encoding='UTF-8') as f:
    json_res = json.load(f)

with open(dest, 'w', encoding='UTF-8') as f:
    csv_writer = csv.writer(f, delimiter=',', quotechar='`', quoting=csv.QUOTE_MINIMAL)
    heads = json_res[0].keys()
    csv_writer.writerow(heads)
    rows = [list(x.values()) for x in json_res]
    csv_writer.writerows(rows)
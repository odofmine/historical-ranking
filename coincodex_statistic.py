import json
import glob
import datetime
import calendar

def write_json(file_name, data):
    with open(f'./coincodex/{file_name}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

json_files = sorted(glob.glob('./coincodex/daily/*_statistic.json'))

market_caps = []
volumns = []
gainers_vs_losers = {'gainers': [], 'losers': []}
turnovers = []

for json_file in json_files:
    dt_string = json_file[-23:-15]
    print(dt_string)
    dt = datetime.datetime.strptime(dt_string, '%Y%m%d').date()
    ts = calendar.timegm(dt.timetuple())

    with open(json_file, 'r', encoding='utf-8') as f:
        statistic = json.load(f)

        market_caps.append([ts, statistic['market_cap']['close']])
        volumns.append([ts, statistic['volume']])
        gainers_vs_losers['gainers'].append([ts, statistic['gainers_percent']])
        gainers_vs_losers['losers'].append([ts, statistic['losers_percent']])
        turnovers.append([ts, round(statistic['volume'] / statistic['market_cap']['close'], 6)])

write_json('market_caps', market_caps)
write_json('volumns', volumns)
write_json('gainers_vs_losers', gainers_vs_losers)
write_json('turnovers', turnovers)
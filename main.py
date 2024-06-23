import subprocess
import random
import pandas as pd
from pandas import ExcelWriter
import json
import openpyxl

# Get a list of wallets
with open('wallets.txt', 'r') as file:
    wallets = file.read().splitlines()
# Get a list of proxies
with open('proxy.txt', 'r') as file:
    proxies = file.read().splitlines()

# List for output data
data = []

for wallet, proxy in zip(wallets, proxies):
    # Select a proxy
    proxy = f"http://{proxy}"

    #Command to be executed in cmd
    curl_command = f'curl -x {proxy} "https://rubyscore.io/api/dashboard/zora/{wallet}" -H "user-agent: Safari/{random.randint(1, 999)}.36"'

    # Run command in cmd
    process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    #Processing of the obtained data
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        data.append(json.loads(stdout.decode()))
        print("Output:\n", stdout.decode())
    else:
        print("Error:\n", stderr.decode())

# Processing the data
processed_data_list = []
for entry in data:
    result = entry['result']
    processed_data = {
        'address': result['address'],
        'chain_id': result['chain_id'],
        'total_spent_gas': result['total_spent_gas']['value'],
        'outgoing_txs_count': result['outgoing_txs_count']['value'],
        'unique_contracts_count': result['unique_contracts_count']['value'],
        'unique_days_count': result['unique_days_count']['value'],
        'unique_weeks_count': result['unique_weeks_count']['value'],
        'unique_months_count': result['unique_months_count']['value'],
        'volume': result['volume']['value'],
        'total_balance_usd': result['total_balance_usd']['value'],
        'total_score': result['total_score'],
        'current_leaderboard_position': result['leaderboard_position']['current'],
        'max_leaderboard_position': result['leaderboard_position']['max']
    }
    processed_data_list.append(processed_data)

df = pd.DataFrame(processed_data_list)

excel_file = 'output.xlsx'
with ExcelWriter(excel_file) as writer:
    df.to_excel(writer, index=False)

print(f"Excel file '{excel_file}' created.")
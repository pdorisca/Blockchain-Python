import subprocess
import json
import os
from constants import *
from dotenv import load_dotenv
from web3 import Web3
from pathlib import Path
from getpass import getpass
from eth_account import Account
from bit import wif_to_key
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3.auto.gethdev import w3

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

mnemonic = os.getenv('MNEMONIC')


def derive_wallets(coin):
    command = f"./derive -g --mnemonic='{mnemonic}' --cols=path,address,privkey,pubkey --format=json --coin='{coin}' --numderive= 2"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return keys

INDEX = 0
coins = {ETH: derive_wallets(ETH), BTCTEST: derive_wallets(BTCTEST)}
#print(coins)

#print(w3.eth.blockNumber)
#print(w3.eth.getBalance('0xfa554F78AeF8b476799C6E2752a9263268C6B1d5'))

print(coins[BTCTEST][0][‘privkey’])
#print(coins[ETH][0]['privkey'])


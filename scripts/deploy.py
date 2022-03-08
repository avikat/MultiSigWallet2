import json
from scripts.helpful_scripts import get_account,get_contract
from brownie import network,config,MultiSigWallet
from web3 import Web3
import yaml
import json
import os
import shutil


def deploy_multisigwallet():
    account =get_account()
    admin = get_account()
    owner = [get_account()]
    multisigwallet = MultiSigWallet.deploy(owner,admin,{"from": account})
    
def 
def main():
    deploy_multisigwallet()


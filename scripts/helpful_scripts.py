from decimal import Decimal
from brownie import Contract, accounts,network,config
from web3 import Web3
FORKED_LOCAL_ENVIROMENTS=["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development","ganache-local"]

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)

    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS or network.show_active() in FORKED_LOCAL_ENVIROMENTS):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])





def get_contract(contract_name):
    # """"This function will grab the address and give us project
    # """
    contract_type = contract_to_mock[contract_name]


    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        if len(contract_type) <=0:
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]

        contract=Contract.from_abi(contract_type._name,contract_address,contract_type.abi)
    return contract
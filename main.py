from web3 import Web3
from Modules import setter
import json 
from solcx import compile_standard
from web3.contract import ConciseContract
from pprint import pprint


mainet = 0
ropsten = 1
kovan = 2
goerli = 3
rinkeby = 4
localhost = 5

entorno_URL = [ "https://mainnet.infura.io/v3/" , \
                "https://ropsten.infura.io/v3/", \
                "https://kovan.infura.io/v3/", \
                "https://goerli.infura.io/v3/", \
                "https://rinkeby.infura.io/v3/", \
                "http://localhost:8545"]
########################################
############# Acciones #################
########################################

conection = 1
entorno = ropsten
transferEther = 0
Deploy = 1
getValue = 0
setValue = 0
checkEvent = 0
########################################






with open('Users.json') as json_file:  
    data = json.load(json_file)

####################################
############# Test #################
####################################



####################################
########### Conexion ###############
####################################
conection = 1
entorno = ropsten

if (conection == 1):

    if (entorno == localhost):
        URL = entorno_URL[entorno]
    else:
        URL = entorno_URL[entorno] + data["Infura"]["projectID"]

    data["Ethereum"]["0"]["address"]
    w3 = Web3(Web3.HTTPProvider(URL))    

    print(w3.isConnected())


    #print(w3.eth.getBlock(12345))

####################################
######## Transfer Ethers ###########
####################################


transferEther = 0
amount = 0.002
_to = data["Ethereum"]["1"]["address"]

if (transferEther == 1):
    print("gas Value", w3.eth.gasPrice)

    signed_txn = w3.eth.account.signTransaction(dict(
        nonce    = w3.eth.getTransactionCount(data["Ethereum"]["0"]["address"]),
        gasPrice = w3.eth.gasPrice, 
        gas      = 21000,
        to       =_to,
        value    = w3.toWei(amount,'ether')
      ),
      data["Ethereum"]["0"]["priv"])

    Tx =  w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(Tx)
    print("transaction pending")

####################################
########### Deploy_RAW #############
####################################

if (Deploy == 1):
    with open('contracts/StoreVar.sol', 'r') as file:
        Contract_Source = file.read() #.replace('\n', '')
    with open('contracts/StoreVar.ABI', 'r') as file:
        Contract_ABI = file.read() #.replace('\n', '')
    with open('contracts/StoreVar.Bytecode', 'r') as file:
        Contract_Bytecode = json.load(file) #.replace('\n', '')
    _data = "0x" + Contract_Bytecode["object"]
    #pprint(Contract_Bytecode["object"])
    #exit()
    signed_txn = w3.eth.account.signTransaction(dict(
            nonce    = w3.eth.getTransactionCount(data["Ethereum"]["0"]["address"]),
            gasPrice = w3.eth.gasPrice, 
            gas      = w3.eth.estimateGas(dict(data= _data)),
            data     = _data
            #to=_to, #0x0
            #value=w3.toWei(amount,'ether')
          ),
          data["Ethereum"]["0"]["priv"])
    # For new deployment of contract it is the bytecode and the encoded arguments. 

    #
    Tx =  w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    pprint(Tx)


####################################
########### setValue ###############
####################################
if (setValue==1):
    _contract_address = "0x3dB1752eF1B8514007725753078166Ec4BE56F0D"
    _data = "0x" + Contract_Bytecode["object"]
    with open('contracts/StoreVar.ABI', 'r') as file:
        Contract_ABI = file.read() #.replace('\n', '')
    signed_txn = w3.eth.account.signTransaction(dict(
        nonce    = w3.eth.getTransactionCount(data["Ethereum"]["0"]["address"]),
        gasPrice = w3.eth.gasPrice, 
        gas      = w3.eth.estimateGas(dict(data= _data,to=_contract_address)),
        data     = "0x" + Contract_Bytecode["object"],
        to       = _contract_address, #0x0
        #value=w3.toWei(amount,'ether')
      ),
      data["Ethereum"]["0"]["priv"])
    # For new deployment of contract it is the bytecode and the encoded arguments. 

    #
    Tx =  w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    pprint(Tx)


    pass

####################################
########### getValue ###############
####################################
if (getValue==1):
    pass



















#result = compile_standard({    'language': 'Solidity',        'sources': {            'StoreVar': {                'content': contract_source_code,            },        },        'outputSelection': {            "*": {"*": ["evm.bytecode.object"]},        },})





#compiled_sol = compile_standard({
#                'language': 'Solidity',
#                'sources': {
#                    'StoreVar.sol':{},
#                    'StoreBar':{'content': contract_source_code}
#                }
#        })
print("///////////////////////////")

#contract_interface = compiled_sol['<stdin>:StoreVar']


#object_methods = [method_name for method_name in dir(compiled_sol)
                  #if callable(getattr(compiled_sol, method_name))]
#print(object_methods)
#Contract_instance = w3.eth.contract(
#    abi=contract_interface['abi'],
#    bytecode=contract_interface['bin'])


#print(Contract_instance)



    #contract_interface = compiled_sol['<stdin>:StoreVar']
#    StoreVar = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
#    tx_hash = StoreVar.constructor().transact()
#    print("tx_hash", tx_hash)
#    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#    print("tx_receipt", tx_receipt)
#    storeVar = w3.eth.contract(
#        address=tx_receipt.contractAddress,
#        abi=contract_interface['abi'],
#    )

#    print('Default contract greeting: {}'.format(
#        storeVar.functions.getVar().call()
#    ))


pass
#setter.main()
#print("conectado", connected)

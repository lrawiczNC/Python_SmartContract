from web3 import Web3
from Modules import setter
import json 


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


entorno = ropsten

with open('Users.json') as json_file:  
    data = json.load(json_file)




if (entorno == localhost):
	URL = entorno_URL[entorno]
else:
	URL = entorno_URL[entorno] + data["Infura"]["projectID"]

data["Ethereum"]["0"]["address"]
w3 = Web3(Web3.HTTPProvider(URL))	

print(w3.isConnected())


print(w3.eth.getBlock(12345))

####################################
######## Transfer Ethers ###########
####################################

print("gas Value", w3.eth.gasPrice)

signed_txn = w3.eth.account.signTransaction(dict(
    nonce=w3.eth.getTransactionCount(data["Ethereum"]["0"]["address"]),
    gasPrice = w3.eth.gasPrice, 
    gas = 100000,
    to=data["Ethereum"]["1"]["address"],
    value=w3.toWei(0.02,'ether')
  ),
  data["Ethereum"]["0"]["priv"])

w3.eth.sendRawTransaction(signed_txn.rawTransaction)


print("transaction pending")

#setter.main()
#print("conectado", connected)

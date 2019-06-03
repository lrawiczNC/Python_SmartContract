from web3 import Web3
from Modules import setter
import json 


mainet = 0
ropsten = 1
kovan = 2
goerli = 3
rinkeby = 4
localhost = 5


entorno = ropsten

with open('Users.json') as json_file:  
    data = json.load(json_file)


entorno_URL = [ "https://mainnet.infura.io/v3/" , \
			 	"https://ropsten.infura.io/v3/", \
				"https://kovan.infura.io/v3/", \
				"https://goerli.infura.io/v3/", \
				"https://rinkeby.infura.io/v3/", \
				"http://localhost:8545"]


if (entorno == localhost):
	URL = entorno_URL[entorno]
else:
	URL = entorno_URL[entorno] + data["Infura"]["projectID"]


web3 = Web3(Web3.HTTPProvider(URL))	

print(web3.isConnected())


print(web3.eth.getBlock(12345))






#setter.main()
#print("conectado", connected)

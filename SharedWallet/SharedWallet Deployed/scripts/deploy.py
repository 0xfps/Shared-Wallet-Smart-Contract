from brownie import SharedWallet, accounts, network, config

def deploy():
    acc = getAccount()
    print("Deploying")
    g = SharedWallet.deploy({"from": acc}, publish_source=True)
    print(f"Deployed at {g.address}")
    
    
    link = "https://rinkeby.etherscan.io/address/"
    
    with open("../Deployment Address.txt", "a+") as r:
        r.write(f"SharedWallet => {link}{g.address}")
    
    print ("Tetelesti")
    
def getAccount():
    if(network.show_active() == "development"):
        acc = accounts[0]
    else:
        acc = accounts.add(config["wallet"]["from_key"])
    
    return acc

def main():
    deploy()
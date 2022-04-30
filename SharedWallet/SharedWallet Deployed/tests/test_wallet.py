from brownie import SharedWallet, accounts, network, reverts, config

def getAccount():
    acc = accounts[0]
    return acc
    

def deploy():
    acc = getAccount()
    dep = SharedWallet.deploy({"from":acc})
    return dep


def testDeploy():
    deps = deploy()
    

def testAdd():
    acc = getAccount()
    deps = deploy()
    
    owner = "0x5e078E6b545cF88aBD5BB58d27488eF8BE0D2593"
    
    deps.addOwner(accounts[8], {"from": owner})
    deps.addOwner(accounts[7], {"from": owner})
    deps.addOwner(accounts[6], {"from": owner})
    

def testRemove():
    acc = getAccount()
    deps = deploy()
    
    owner = "0x5e078E6b545cF88aBD5BB58d27488eF8BE0D2593"
    
    deps.removeOwner(accounts[8], {"from": owner})
    

def testDeposit():
    acc = getAccount()
    deps = deploy()
    
    owner = "0x5e078E6b545cF88aBD5BB58d27488eF8BE0D2593"
    
    deps.deposit({"from": acc, "value": "10 ether"})
    

def testWithdraw():
    acc = getAccount()
    deps = deploy()
    
    owner = "0x5e078E6b545cF88aBD5BB58d27488eF8BE0D2593"
    
    deps.deposit({"from": acc, "value": "10 ether"})
    deps.withdraw("300 gwei", {"from": owner});
    

def testApprove():
    
    acc = getAccount()
    deps = deploy()
    
    owner = "0x5e078E6b545cF88aBD5BB58d27488eF8BE0D2593"
    
    deps.addOwner(accounts[8], {"from": owner})
    deps.addOwner(accounts[7], {"from": owner})
    deps.addOwner(accounts[6], {"from": owner})
    
    deps.deposit({"from": acc, "value": "10 ether"})
    deps.withdraw("300 gwei", {"from": owner});
    
    deps.approveWithdrawal(owner, {"from": accounts[7]})


def testClose():
    
    acc = getAccount()
    deps = deploy()
    
    owner = "0x5e078E6b545cF88aBD5BB58d27488eF8BE0D2593"
    
    deps.deposit({"from": acc, "value": "10 ether"})
    
    
    deps.withdraw("300 gwei", {"from": owner});
    deps.closeWithdrawal({"from":owner})
    

def testSee():
    acc = getAccount()
    deps = deploy()
    
    owner = "0x5e078E6b545cF88aBD5BB58d27488eF8BE0D2593"
    
    deps.deposit({"from": accounts[9], "value": "10 ether"})
    
    deps.withdraw("300 gwei", {"from": owner});
    
    num = deps.viewWithdrawals(owner, {"from":owner})
    
    assert num == "300 gwei"
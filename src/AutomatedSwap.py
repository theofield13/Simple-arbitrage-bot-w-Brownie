import time
import datetime
import sys

import brownie
from brownie import *


network.connect("avax-main")
user = accounts.load("test_account")


print("Loading Contract:")
dai_contract = Contract.from_explorer("0xd586e7f844cea2f87f50152665bcbc2c279d8d70")
mim_contract = Contract.from_explorer("0x130966628846bfd36ff31a822705796e8cb8c18d")
wavax_contract = Contract.from_explorer("0xb31f66aa3c1e785363f0875a1b74e27b85fd66c7")
router_contract = Contract.from_explorer("0x60aE616a2155Ee3d9A68541Ba4544862310933d4")


dai = {
    "address": dai_contract.address,
    "symbol": dai_contract.symbol(),
    "decimals": dai_contract.decimals(),
    "balance": dai_contract.balanceOf(user.address),
}

mim = {
    "address": mim_contract.address,
    "symbol": mim_contract.symbol(),
    "decimals": mim_contract.decimals(),
    "balance": mim_contract.balanceOf(user.address),
}

print(dai)
print(mim)

if mim["balance"] == 0:
    sys.exit("MIM balance is zero, aborting...")

if mim_contract.allowance(user.address, router_contract.address) < mim["balance"]:
    mim_contract.approve(
        router_contract.address,
        mim["balance"],
        {"from": user.address},
    )

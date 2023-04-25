import os
import math
import sys
from netaddr import IPAddress

print("Please enter your subnet mask:")
subnetMask = input()

subnetMaskList = subnetMask.split(".")

temp = list()
for i in subnetMaskList:
    temp.append(str(bin(int(i))).count("1"))
print("Your subnet mask in CIDR format is: /"+str(sum(temp)))
    
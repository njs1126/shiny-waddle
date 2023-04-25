import os
import math
import sys
from netaddr import IPAddress

# Globally defined variables
cidr = ""
subnetMask = ""
ipAddress = ""
hosts = ""
poss_SubnetMasks = [255,254,252,248,240,224,192,128,0]

print("Choose an option for your subnetting\n")
print("(1) CIDR\n")
print("(2) Subnet Mask\n")
choice = int(input())

# Driver code
if(choice==1):
    print("Enter CIDR notation, example: 24\n")
    print("CIDR number: ")
    cidrChoice = int(input())

if(choice==2):
    print("Enter Subnet Mask: ")
    subnetMaskChoice = input()

    # Type Casting
    newSubnetMask = subnetMaskChoice.split(".")
    for i in range(0, len(newSubnetMask)):
        newSubnetMask[i] = int(newSubnetMask[i])
    
    q1 = newSubnetMask[0]
    q2 = newSubnetMask[1]
    q3 = newSubnetMask[2]
    q4 = newSubnetMask[3]

    # Input Validation
    wrongMaskCount = 0
    for x in range(len(poss_SubnetMasks)):  
        if(poss_SubnetMasks[x] == q1 or poss_SubnetMasks[x] == q2 or poss_SubnetMasks[x] == q3 or poss_SubnetMasks[x] == q4):
            print("valid subnet mask at position: " + str(poss_SubnetMasks[x]))
        else:
            print("invalid subnet mask at position: " + str(poss_SubnetMasks[x]))
            wrongMaskCount+=1
            break

    if(wrongMaskCount == 0):
        print("Your subnet mask in CIDR notation is: {}".format(IPAddress(subnetMaskChoice).netmask_bits()))
    else:
        sys.exit()
    
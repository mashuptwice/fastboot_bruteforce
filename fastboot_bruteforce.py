#!/usr/bin/env python3

# 2021 by mashuptwice

#script to bruteforce 16 digit huawei bootloader unlock code
#not fast but better than huawei's solution (none)

import random
import subprocess

foundcode = "false"
counter = 1


while foundcode == "false":


    #generate random 16 digit code
    number="%016d" % random.randint(0,9999999999999999)
    code = str(number)
    #print("current code:")
    #print(code)

    output = subprocess.run(["fastboot", "oem", "unlock", code], capture_output=True)
    #output = subprocess.run(["fastboot", "reboot", "bootloader"], capture_output=True)
    output = str(output)

    print(output)

    counter = counter + 1
    if "Invalid" in output:
        print("tried " + str(counter) + " times")
    else:
        print("found code?!")
        print(code)
        foundcode = "true"
        f = open("agsw09_code", "a")
        f.write(output + code)
        f.close()
        break

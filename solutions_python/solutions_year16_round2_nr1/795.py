#-------------------------------------------------------------------------------
# Name:        Getting the Digits
# Purpose:
#
# Author:      udonko
#
# Created:     01/05/2016
# Copyright:   (c) udonko 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys

from collections import Counter
def resolve(text):
    digits=[]

    charcount =Counter(text)

    if "Z" in charcount:
        num = charcount["Z"]
        digits.extend([0 for i in range(num)])
        charcount["E"] -= num
        charcount["R"] -= num
        charcount["O"] -= num
        charcount["Z"] = 0
    if "X" in charcount:
        num = charcount["X"]
        digits.extend([6 for i in range(num)])
        charcount["I"] -= num
        charcount["S"] -= num
        charcount["X"] = 0
    if "W" in charcount:
        num = charcount["W"]
        digits.extend([2 for i in range(num)])
        charcount["T"] -= num
        charcount["O"] -= num
        charcount["W"] = 0
    if "U" in charcount:
        num = charcount["U"]
        digits.extend([4 for i in range(num)])
        charcount["F"] -= num
        charcount["O"] -= num
        charcount["R"] -= num
        charcount["U"] = 0
    if "G" in charcount:
        num = charcount["G"]
        digits.extend([8 for i in range(num)])
        charcount["E"] -= num
        charcount["I"] -= num
        charcount["H"] -= num
        charcount["T"] -= num
        charcount["G"] = 0
    if "F" in charcount and charcount["F"] > 0:
        num = charcount["F"]
        digits.extend([5 for i in range(num)])
        charcount["I"] -= num
        charcount["V"] -= num
        charcount["E"] -= num
        charcount["F"] = 0
    if "V" in charcount and charcount["V"] > 0:
        num = charcount["V"]
        digits.extend([7 for i in range(num)])
        charcount["S"] -= num
        charcount["E"] -= num * 2
        charcount["N"] -= num
        charcount["V"] = 0
    if "R" in charcount and charcount["R"] > 0:
        num = charcount["R"]
        digits.extend([3 for i in range(num)])
        charcount["T"] -= num
        charcount["H"] -= num
        charcount["E"] -= num*2
        charcount["R"] = 0
    if "O" in charcount and charcount["O"] > 0:
        num = charcount["O"]
        digits.extend([1 for i in range(num)])
        charcount["N"] -= num
        charcount["E"] -= num
        charcount["O"] = 0
    if "I" in charcount and charcount["I"] > 0:
        num = charcount["I"]
        digits.extend([9 for i in range(num)])
    digits.sort()
    return "".join(list(map(str, digits)))
def main():
    with open("A-large (1).in","r") as infile:
        with open("outGetting the Digits.txt","w") as outfile:
            n = int(infile.readline())
            for i in range(n):
                text=infile.readline().strip()
                result = resolve(text)

                outtxt="Case #{0}: {1}\n".format(i+1, result)
                outfile.write(outtxt)


if __name__ == '__main__':
    main()

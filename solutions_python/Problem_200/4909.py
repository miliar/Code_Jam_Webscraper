import sys
import os
from sys import stdin

def tidyNum(n):
    ns = str(n)
    if checkTidy(n) == True:
        return n
    
    for i in range(n, -1, -1):
        if checkTidy(i) == True:
            return i
        else:
            pass

def checkTidy(n):
    n2 = str(n)
    for i in range(len(n2)-1):
        if int(n2[i]) <= int(n2[i+1]):
            pass
        else:
            return False
    return True


cf = open("B-small-attempt4.in", "r")
l = []
for i in cf:
    l.append(int(i))
cf.close()

del l[0]
print(len(l))

cc = 1
f = open("n.out","w")
for i in l:
    f.write("Case #" + str(int(cc)) + ": " + str(tidyNum(int(i))) + "\n")
    cc += 1
    

f.close()

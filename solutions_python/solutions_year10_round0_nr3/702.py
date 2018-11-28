import os
import sys
import math

def final(path=os.path.expanduser("~")+"/"+"gcj/"):
    fin=open(path+"C-small-attempt0.in", "r")
    fout = open(path+"C-small.out", "w")

    test_cases = fin.readline().strip()
    
    for i in range(int(test_cases)):
        dim = fin.readline().strip().split(" ")
        groups = fin.readline().strip().split(" ")

        r = int(dim[0])
        k = int(dim[1])
        n = int(dim[2])

        amount = 0
        
        for j in range(r):
            temp = 0
            count = 0
            while (((temp + int(groups[0])) <= k) and (count < n)):
                temp = temp + int(groups[0])
                val = groups.pop(0)
                groups.append(val)
                count = count + 1
            amount = amount + temp
    

        fout.write("Case #"+str(i+1)+": "+str(amount)+"\n")

    fout.close()
    fin.close()



final()

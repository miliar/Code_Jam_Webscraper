import os
import math
import types

def main():
    all_valid_nums = []
    idx = 0
    f = open("A-small-attempt0.in","r")
    #f = open("trial.txt","r")
    doc = f.read().split('\n')   
    num_test_cases = int(doc[idx])
    for i in range(1,(num_test_cases+1)):
        idx = idx+1
        ips = doc[idx].split(" ")
        r = int(ips[0])
        t = int(ips[1])
        tot_rings = 0
        while(t>0):
            needed = pow((r+1),2) - pow(r, 2)
            if(needed < t) or (needed == t): 
                #print "Needed: "+str(needed)+" t:"+str(t)
                t = t-needed
                tot_rings = tot_rings+1
            else:
                t = 0
            r = r+2
        print "Case #"+str(i)+": "+str(tot_rings)
            
            
if __name__ == "__main__":
    main()


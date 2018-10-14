import os
import sys
import math

def final(path=os.path.expanduser("~")+"/"+"/Desktop/gcj/"):
    fin=open(path+"C-small-attempt0.in", "r")
#    fin=open(path+"test.txt", "r")
    fout = open(path+"A-small.out", "w")

    test_cases_count = fin.readline().strip()
#    print "No of test characters == %s" % test_cases_count
    
    for i in range(int(test_cases_count)):
        dimension = fin.readline().strip().split(" ")
#        print "dim %s" % dimension
        groups = fin.readline().strip().split(" ")

        r = int(dimension[0])
        k = int(dimension[1])
        n = int(dimension[2])

        euro = 0
        
        for j in range(r):
            temp = 0
            count = 0
            while (((temp + int(groups[0])) <= k) and (count < n)):
                temp = temp + int(groups[0])
                tempval = groups.pop(0)
                groups.append(tempval)
                count = count + 1
            euro = euro + temp
#            print temp
    
#        print "Case #%s: %s" % (i+1, euro)
        fout.write("Case #"+str(i+1)+": "+str(euro)+"\n")

    fout.close()
    fin.close()



final()

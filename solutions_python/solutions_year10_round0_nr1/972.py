import os
import sys
import math

def final(path=os.path.expanduser("~")+"/"+"/Desktop/gcj/"):
    fin=open(path+"A-small-attempt0.in", "r")
#    fin=open(path+"test.txt", "r")
    fout = open(path+"A-small.out", "w")

    test_cases_count = fin.readline().strip()
#    print "No of test characters == %s" % test_cases_count
    
    for i in range(int(test_cases_count)):
        dimension = fin.readline().strip().split(" ")
#        print "dim %s" % dimension

        maxval = int(math.pow(2,30))

        val = int(math.pow(2,int(dimension[0]))) - 1
        snap = int(dimension[1])

        if (snap < val):
            outval = "OFF"
        elif (snap == val):
            outval = "ON"
        elif (snap > val):
            outval = "OFF"
            initval = val 
            while(snap > val):
                val = (val + initval) + 1
                if (snap == val):
                    outval = "ON"
                    break;

#        print "Case #%s: %s" % (i+1, outval)
        fout.write("Case #"+str(i+1)+": "+outval+"\n")

    fout.close()
    fin.close()



final()

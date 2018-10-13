import os
import sys
import math

def fsnapper(path=os.path.expanduser("~")+"/"+"gcj/"):
    fin=open(path+"A-large.in", "r")
#    fin=open(path+"test.txt", "r")
    fout = open(path+"A-large.out", "w")

    test_cases = fin.readline().strip()
    
    for i in range(int(test_cases)):
        dim = fin.readline().strip().split(" ")

        maxval = int(math.pow(2,30))

        val = int(math.pow(2,int(dim[0]))) - 1
        snap = int(dim[1])

        if (snap < val):
            oval = "OFF"
        elif (snap == val):
            oval = "ON"
        elif (snap > val):
            oval = "OFF"

            quo = snap / val
            tquo = quo / val
            if (quo > 1):
                actual = (val*(quo-tquo)) + (quo-1 - tquo)
                if (actual == snap):
                    oval = "ON"
                else:
                    while (actual < snap):
                        actual = actual + val + 1
                        if (actual == snap):
                            oval = "ON"
                            break
#        print "Case #%s: %s" % (i+1, oval)
        fout.write("Case #"+str(i+1)+": "+oval+"\n")

    fout.close()
    fin.close()



fsnapper()

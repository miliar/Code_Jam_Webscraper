import os
import sys
import math

def final(path=os.path.expanduser("~")+"/"+"/Desktop/gcj/"):
    fin=open(path+"A-large.in", "r")
#    fin=open(path+"test.txt", "r")
    fout = open(path+"A-large.out", "w")

    test_cases_count = fin.readline().strip()
#    print "No of test characters == %s" % test_cases_count
    
    for i in range(int(test_cases_count)):
        n = fin.readline().strip().split(" ")

        left = []
        right = []
        lefts = []
        count = 0
        for j in range(int(n[0])):
            dim = fin.readline().strip().split(" ")
            left.append(int(dim[0]))
            lefts.append(int(dim[0]))
            right.append(int(dim[1]))

        lefts.sort()
        

        for k in range(int(n[0])):
            temp1 = left[k]
            temp2 = right[k]

            pos = lefts.index(temp1)

            for j in range(pos+1,int(n[0])):

                pos1 = left.index(lefts[j])
                if ((left[pos1] > temp1) and (right[pos1] < temp2)) :
                        count = count + 1

 #       print "Case #%s: %s" %(str(i+1), str(count))
                            
        
        fout.write("Case #"+str(i+1)+": "+str(count)+"\n")

    fout.close()
    fin.close()



final()

import sys
import pdb 
                              
with open("qa.in") as f:
    fout = open("qa.out", "w")
    ttt = [int(x) for x in f.readline().split()][0]
    for tt in range(1, ttt + 1):
        x1 = [int(x) for x in f.readline().split()][0]
        a1 = []
        for i in range(0, 4):
            a1.append(set([int(x) for x in f.readline().split()]))
        x2 = [int(x) for x in f.readline().split()][0]
        a2 = []
        for i in range(0, 4):
            a2.append(set([int(x) for x in f.readline().split()]))
        s = a1[x1 - 1] & a2[x2 - 1]
        fout.write("Case #%d: " % tt)
        if(len(s) == 0):
            fout.write("Volunteer cheated!\n")
        elif(len(s) > 1):
            fout.write("Bad magician!\n")
        else:
            r = [x for x in s][0]
            fout.write("%d\n" % r)
    fout.close()

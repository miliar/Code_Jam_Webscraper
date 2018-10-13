'''
Created on Apr 10, 2015

@author: billyanhuang
'''
fin = open('D-small-attempt5.in', 'r')
fout = open('D-small-attempt5.out', 'w')
T = int(fin.readline())
for i in range(T):
    fout.write("Case #")
    fout.write(str(i+1))
    fout.write(": ")
    inp = fin.readline().split()
    X = int(inp[0])
    R = int(inp[1])
    C = int(inp[2])
    if ((X > R) and (X > C)) or ((X > 2*R) or (X > 2*C)) or (((X > 2*R-1) or (X > 2*C-1)) and (R > 1) and (C > 1)):
        fout.write("RICHARD")
        #print str(X) + " " + str(R) + " " + str(C) + " " + "RICHARD" + "x"
    else:
        if (R*C)%X == 0:
            fout.write("GABRIEL")
            #print str(X) + " " + str(R) + " " + str(C)
        else:
            fout.write("RICHARD")
            #print str(X) + " " + str(R) + " " + str(C) + " " + "RICHARD"
    fout.write("\n")
fout.close()
    
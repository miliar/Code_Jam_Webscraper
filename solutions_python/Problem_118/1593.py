#codejam 2013
#problem C

import math

f = open("C-large-1.in", "r")
fout = open("output.txt", "w")
fnum = open("b002779.txt", "r")

tot = f.readlines()
totnum = fnum.readlines()

#print(tot)
#print(totnum)

T = int(tot[0])
ind = 0
for line in range(1,T+1):
    ind += 1
    i = 0
    cline = tot[line].split()
    #print(cline)
    min_x = int(cline[0])
    max_x = int(cline[1])
    for x in totnum:
        if ((min_x <= int(x)) and (max_x >= int(x))):
            y=str(int(math.sqrt(float(x))))
            #print(y)
            if(y==y[::-1]):
                i+=1
    fout.write("Case #" + str(ind) + ": " + str(i) + "\n")
fout.close()

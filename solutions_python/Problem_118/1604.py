#codejam 2013
#problem C

import math

f = open("C-large-1.in", "r")
writer = open("output.txt", "w")
read2 = open("b002779.txt", "r")

inp = f.readlines()
inpnum = read2.readlines()

#print(inp)
#print(inpnum)

T = int(inp[0])
ind = 0
for line in range(1,T+1):
    ind += 1
    i = 0
    cline = inp[line].split()
    #print(cline)
    min_x = int(cline[0])
    max_x = int(cline[1])
    for x in inpnum:
        if ((min_x <= int(x)) and (max_x >= int(x))):
            y=str(int(math.sqrt(float(x))))
            #print(y)
            if(y==y[::-1]):
                i+=1
    writer.write("Case #" + str(ind) + ": " + str(i) + "\n")
writer.close()

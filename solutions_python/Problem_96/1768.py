from __future__ import division
from math import ceil
fr = open("inbig.in", "r")
fw = open("outbig.txt","w")
lines = int(fr.readline())
for i, l in enumerate(fr.xreadlines()):
    if i < lines:
        count = 0
        fw.write("Case #" + str(i + 1) + ": ")
        t = l.split()
        num = int(t[0])
        sup = int(t[1])
        imin = int(t[2])
        for i2 in range (0, num):
            temp = ceil(int(t[i2+3])/3)
            if temp >= imin:
                count += 1
            elif temp == imin-1 and (int(t[i2+3]) % 3 == 2 or  int(t[i2+3]) % 3 == 0) and sup > 0 and int(t[i2+3]) > 0:
                sup -= 1
                count += 1
        fw.write(str(count))
        if not i == lines - 1:
            fw.write("\n")
fw.close()
fr.close()

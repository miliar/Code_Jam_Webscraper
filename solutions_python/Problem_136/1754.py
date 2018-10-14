import math
import re
file1 = open('B-small-attempt0.in', 'r')
wf = open('outputBsmall.out', 'w')
t = file1.readline()
print t
for i in range(int(t)):
    str1 = file1.readline()
    s1=re.split(' |, |\*|\n',str1)
    print s1
    c = float(s1[0])
    f = float(s1[1])
    x = float(s1[2])
    n = 1
    oldv = x/2.0
    while(True):
        val = 0
        for k in range(n):
            val += c/(2+f*(k))
        val += x/(2+f*n)
        if val < oldv:
            oldv = val
            n += 1
        else:
            break
    ans = oldv
    wf.write('Case #'+str(i+1)+': '+str(ans)+'\n')



file1.close()
wf.close()

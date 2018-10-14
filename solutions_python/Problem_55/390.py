#
import re
import math
f = open("C-small-attempt0.in","r")
fo = open("C-small-attempt0.out","w")

lines = f.readlines()
lines = [l.strip() for l in lines]
nlines = len(lines)
i = 0
T = int(lines[i])
for icase in range(T):
    # set parameters
    i = i + 1
    l = re.split(" ",lines[i])
    [R,k,N] = [int(x) for x in l[:3]]
    i = i + 1
    l = re.split(" ",lines[i])
    g = [int(x) for x in l[:N]]
    ir = 0
    j = 0
    income = 0
    room = k
    igroup = 0
    while ir < R:
        if (room >= g[j]) and ( igroup < N ):
            igroup = igroup + 1
            room = room - g[j]
            income = income + g[j]
            j = (j+1)%N
        else:
            ir = ir + 1
            igroup = 0
            room = k      
        
    print("Case #",icase+1,": ",income,sep="",file=fo)
    print("Case #",icase+1,": ",income,sep="")


#print("Case #",icase+1,": ",nswitch,sep="",file=fo)
f.close()
fo.close()


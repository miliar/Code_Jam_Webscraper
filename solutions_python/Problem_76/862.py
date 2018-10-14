from itertools import *

inf=open('cjc_input_sm.txt','r')
ouf=open('cjc_output.txt','w')
cases=int(inf.readline())

for line in range(cases):
    num=int(inf.readline())
    inp=inf.readline().strip('\n')
    inp=inp.split(' ')
    max=0
    for x in range(1,num):
        for c in combinations(range(len(inp)),x):
            s1,s2=0,0
            s=0
            for x in range(len(inp)):
                if x in c:
                    s1=s1^int(inp[x])
                    s+=int(inp[x])
                else: s2=s2^int(inp[x])
            if s1==s2 and s>max:
                max=s
    ouf.write('Case #'+str(line+1)+': ')
    if max==0: ouf.write('NO\n')
    else: ouf.write(str(max)+'\n')

ouf.close()
inf.close()

"""
Google Code Jam
    Qualification Round 2010
        B. Fair Warning
            small in
"""

import fractions

name="B-small-attempt2"

def delta(t):
    d=[]
    for i in range(len(t)-1):
        d.append(t[i+1]-t[i])
    return d

with open(name+'.in','r') as infile:
    cases = int(infile.readline())
    with open(name+'.out2','w') as outfile:
        for i in range(1,cases+1):
            N,t=infile.readline().split(' ',1)
            t=sorted(set(map(int,t.split(' '))))
            d=delta(t)
            if len(d)>1:
                g=fractions.gcd(*d)
            else:
                g=d[0]
            y=(-t[0])%g
            print('Case #',i,': ',y,sep='',file=outfile)


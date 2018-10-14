"""
Google Code Jam
    Qualification Round 2010
        C. Theme Park
            small in
"""

name="C-small-attempt0"

def calMoney(r,k,g):
    s=0
    for j in range(r):
        for i in range(1,len(g)+1):
            if sum(g[:i]) > k:
                i -= 1
                break
        s+=sum(g[:i])
        g=g[i:]+g[:i]
    return s


with open(name+'.in','r') as infile:
    cases = int(infile.readline())
    with open(name+'.out','w') as outfile:
        for case in range(1,cases+1):
            R,K,N=map(int, infile.readline().split(' '))
            G=list(map(int, infile.readline().split(' ')))
            print('Case #',case,': ',calMoney(R,K,G),sep='',file=outfile)


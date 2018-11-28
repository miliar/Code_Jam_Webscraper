"""
Google Code Jam
    Qualification Round 2010
        A. Snapper Chain
            large in
"""

name="A-large"

with open(name+'.in','r') as infile:
    cases = int(infile.readline())
    with open(name+'.out','w') as outfile:
        for i in range(1,cases+1):
            N,K=map(int, infile.readline().split(' '))
            if (K%(1<<N)==((1<<N)-1)):
                print('Case #',i,': ON',sep='',file=outfile)
            else:
                print('Case #',i,': OFF',sep='',file=outfile)

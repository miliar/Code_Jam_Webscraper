"""
Google Code Jam
    Round 1C 2010
        A.
"""

#import 

name="A-large"


with open(name+'.in','r') as infile:
    cases = int(infile.readline())
    with open(name+'.out','w') as outfile:
        for i in range(1,cases+1):
            # parse input
            N=int(infile.readline().strip())
            lines=[]
            for j in range(N):
                lines.append(tuple(map(int,infile.readline().split(' '))))
            # coding here:
            ans = 0
            for l in range(len(lines)):
                for k in lines[l+1:]:
                    if (lines[l][0]>k[0])!=(lines[l][1]>k[1]):
                        ans+=1
            # output the answers
            #print('Case #',i,': ',ans,sep='')
            print('Case #',i,': ',ans,sep='',file=outfile)


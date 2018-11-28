# Welcome to code jam

import random
import pdb
import sys

infile=open(sys.argv[1])

welcome="welcome to code jam"

def count(i,j):
    """Counts the number of times the string welcome[i:] occurs in
    case[j:]
    """
    global welcome, case, table
    
    if table[i][j]!=-1:
        return table[i][j]

    if len(welcome[i:])>len(case[j:]):
        table[i][j]=0
        return table[i][j]

    if i==18:                   # we reached the end of welcome
        table[i][j]=case[j:].count(welcome[18])
        return table[i][j]

    if welcome[i]==case[j]:
        table[i][j]=count(i,j+1)+count(i+1,j+1)
    else:
        table[i][j]=count(i,j+1)        

    return table[i][j]

if __name__ == '__main__':
    N=int(infile.readline())
    for i in range(N):
        case=infile.readline().strip()
        table=[[-1]*len(case) for c in welcome]

        cnt=str(count(0,0))[-4:] # we only want the last four digits
        while len(cnt)!=4:
            cnt='0'+cnt

        print 'Case #%d: %s' % (i+1, cnt)

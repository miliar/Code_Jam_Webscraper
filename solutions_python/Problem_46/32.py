from codejam import *

def run(f):
    n=int(f.next())
    ranks=[]
    for i in range(n):
        row = f.line()[0]
        r=len(row)-1
        while r>=0 and row[r]=='0':
            r-=1
        ranks.append(r)

    count=0
    for i in range(n):
        for j in range(len(ranks)):
            if ranks[j]<=i:
                count += j
                del ranks[j]
                break
        else:
            assert False
    print count
    return

def main(fn):
    f=Reader(fn)
    n=int(f.next())
    for i in range(n):
        print 'Case #%d:'%(i+1), #TODO
        run(f)
    return

import sys
main(*sys.argv[1:])

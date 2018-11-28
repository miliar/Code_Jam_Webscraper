#! /usr/bin/python

#  (c) 2010 Wott (http://wott.net.ru/ , wott@gmail.com)

__author__="Wott"
__date__ ="$08.05.2010 4:53:00$"

import sys

def case(R,k,N,q):
    q*=2 # to cycle
    amount=[0]*N
    next=[-1]*N
    for i in range(N):
        #find amount and next for this case
        for j in range(i,i+N): #from current to last before current
            if amount[i]+q[j]>k: break # if group too big
            amount[i]+=q[j]
            next[i]=(j+1)%N
    p = ret = 0
    for i in range(R):
        ret+=amount[p]
        p=next[p]
        if (p==-1): break # too big group - stop running
    if (p==-1): 
        print("STOP: %d,%d,%d,%s => %s,%s" % (R,k,N,q,amount,next))
    #print("LINE: %d,%d,%d,%s => %s,%s" % (R,k,N,q,amount,next))
    return(ret)

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: %s in.file out.file" % sys.argv[0])
        return
    with open(args[0]) as infile:
        with open(args[1],'w') as outfile:
            T = int(infile.readline())
            for i in range(T):
                R,k,N=[int(i) for i in infile.readline().rstrip().split()]
                queue=[int(i) for i in infile.readline().rstrip().split()]
                c = case(R,k,N,queue)
                outfile.write("Case #%s: %d\n" % (i+1,c))

if __name__ == '__main__':
    main()


#! /usr/bin/python

#  (c) 2010 Wott (http://wott.net.ru/ , wott@gmail.com)

__author__="Wott"
__date__ ="$23.05.2010 14:50:00$"

import sys
import math

def case(L,P,C):
    (l,p,c)=(L,P,C)
    #ret0=int(math.log(p/l,c)) if l*c<p else 0
    ret=0
    while (l*c<p):
        l*=c
        ret+=1
    reti=math.log(ret,2)+1 if ret>0 else 0
    #if ret0!=ret: print("LINE: %d,%d,%d => %d,%d,%d" % (L,P,C,ret,ret0,reti))
    return(reti)

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: %s in.file out.file" % sys.argv[0])
        return
    with open(args[0]) as infile:
        with open(args[1],'w') as outfile:
            T = int(infile.readline())
            for t in range(T):
                L,P,C=[int(i) for i in infile.readline().rstrip().split()]
                c = case(L,P,C)
                print("Case #%d" % t)
                outfile.write("Case #%d: %d\n" % (t+1,c))

if __name__ == '__main__':
    main()

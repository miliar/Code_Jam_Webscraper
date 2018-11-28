#! /usr/bin/python
# -*- coding: euc-jp -*-

import sys

def main():
    cin=sys.stdin
    for t in xrange(int(cin.readline())):
        s=int(cin.readline())
        e={}
        for i in xrange(s):
            e[cin.readline().strip()]=i
            
        q=int(cin.readline())

        ans=0
        v=set()
        for _ in xrange(q):
            str=cin.readline().strip()
            if str in e:
                i=e[str]
                v.add(i)
                if len(v)==s:
                    ans+=1
                    v.clear()
                    v.add(i)
            
        print 'Case #%d: %d'%(t+1,ans)

if __name__=="__main__":
    main()
    

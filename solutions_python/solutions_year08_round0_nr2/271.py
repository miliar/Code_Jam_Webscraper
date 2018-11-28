#! /usr/bin/python

import sys

def time(str):
    return int(str[0:2])*60+int(str[3:5])

def main():
    cin=sys.stdin
    for ca in xrange(int(cin.readline())):
        t=int(cin.readline())
        na,nb=map(int,cin.readline().split())

        que=[]
        for _ in xrange(na):
            i,j=map(time,cin.readline().split())
            que.append((i,1))
            que.append((j+t,-1))
        for _ in xrange(nb):
            i,j=map(time,cin.readline().split())
            que.append((i,2))
            que.append((j+t,-2))

        que.sort()
        a=b=at=bt=0
        for _, v in que:
            if v==1:
                if at>0:
                    at-=1
                else:
                    a+=1
            elif v==-1:
                bt+=1
            elif v==2:
                if bt>0:
                    bt-=1
                else:
                    b+=1                
            elif v==-2:
                at+=1

        print 'Case #%d: %d %d'%(ca+1,a,b)

if __name__=="__main__":
    main()

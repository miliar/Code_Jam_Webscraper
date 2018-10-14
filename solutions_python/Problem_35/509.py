#!/usr/bin/env python
import sys, string, copy
def rl(): return sys.stdin.readline().strip()
def rr(): return map(int,string.split(rl(), " "))

def flow(r,c,mp):
    if(mp[r][c]=='N'):
        mp[r][c]=flow(r-1,c,mp)
    elif(mp[r][c]=='W'):
        mp[r][c]=flow(r,c-1,mp)
    elif(mp[r][c]=="E"):
        mp[r][c]=flow(r,c+1,mp)
    elif(mp[r][c]=="S"):
        mp[r][c]=flow(r+1,c,mp)
    return mp[r][c]

def repc(orig, new, mp):
    for r in range(0,len(mp)):
        for c in range(0,len(mp[r])):
            if mp[r][c]==orig:
                mp[r][c]=new

T=int(rl())
for m in range(0,T):
    libr='abcdefghijklmnopqrstuvwxyz'
    sink=0
    rc=rr()
    mp=[]
    dmp=[]
    for r in range(0,rc[0]):
        mp.append(rr())
    for r in range(0,rc[0]):
        dmp.append([])
        for c in range(0,rc[1]):
            dmp[r].append('')
            nwes=[]
            if(r > 0):
                nwes.append(mp[r-1][c])
            else:
                nwes.append(10)
            
            if(c > 0):
                nwes.append(mp[r][c-1])
            else:
                nwes.append(10)
            
            if(c < rc[1]-1):
                nwes.append(mp[r][c+1])
            else:
                nwes.append(10)
            
            if(r < rc[0]-1):
                nwes.append(mp[r+1][c])
            else:
                nwes.append(10)

            nwes.append(mp[r][c])
            if(nwes[4]==min(nwes)):
                dmp[r][c]=sink
                sink=sink+1
            elif(nwes[0]==min(nwes)):
                dmp[r][c]='N'
            elif(nwes[1]==min(nwes)):
                dmp[r][c]='W'
            elif(nwes[2]==min(nwes)):
                dmp[r][c]='E'
            elif(nwes[3]==min(nwes)):
                dmp[r][c]='S'

    for r in range(0,rc[0]):
        for c in range(0,rc[1]):
            flow(r,c,dmp)
    
    for r in dmp:
        for c in r:
            if(str(c).isdigit()):
                repc(c,libr[0],dmp)
                libr=libr[1:]
    print("Case #"+str(m+1)+": ")
    ou=''
    for r in dmp:
        for c in r:
            ou+=str(c)+' '
        ou.strip()
        ou+='\n'
    sys.stdout.write(ou)


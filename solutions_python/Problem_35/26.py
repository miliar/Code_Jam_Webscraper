import sys
import psyco
psyco.full()

d=[
    (-1,0),
    (0,-1),
    (0,1),
    (1,0)
    ]
alphabet="abcdefghijklmnopqrstuvwxyz"

T=int(sys.stdin.readline())

for tid in range(T):
    H,W=map(int,sys.stdin.readline().split(' '))
    m=[]
    tgt=[]
    lbl=[]
    lblid=0
    for i in range(H):
        m.append(map(int,sys.stdin.readline().split(' ')))
        tgt.append([(i,j) for j in range(W)])
        lbl.append(['']*W)
    
    #Do combination
    for i in range(H):
        for j in range(W):
            grad=((0,0),0)
            for k in d:
                if i+k[0]>=0 and i+k[0]<H and j+k[1]>=0 and j+k[1]<W:
                    ng=m[i+k[0]][j+k[1]]
                    if ng<m[i][j]-grad[1]:
                        grad=(k,m[i][j]-ng)
            if grad[0]!=-1:
                tgt[i][j]=(i+grad[0][0],j+grad[0][1])
    
    #Print & update path
    print "Case #%s:"%(tid+1)
    for i in range(H):
        linelbl=[]
        for j in range(W):
            
            def findroot():
                org=posi=(i,j)
                while tgt[posi[0]][posi[1]]!=posi:
                    posi=tgt[posi[0]][posi[1]]
                while tgt[org[0]][org[1]]!=posi:
                    tmp=tgt[org[0]][org[1]]
                    tgt[org[0]][org[1]]=posi
                    org=tmp
                return posi
            
            def getlabel(posi):
                global lblid
                if lbl[posi[0]][posi[1]]=="":
                    lbl[posi[0]][posi[1]]=alphabet[lblid]
                    lblid+=1
                return lbl[posi[0]][posi[1]]
            
            linelbl.append(getlabel(findroot()))
        print " ".join(linelbl)

import sys

f = "A-small-attempt0.in"
if len(sys.argv) == 2:
    f = sys.argv[1]
    
file = open(f,"r")

t=int(file.readline())

def findNext(pos,l,sn):
    abn = [None,None,None]
    
    a = True
    b = True
    for i in range(pos,sn):
        if a and l[i*2] == "O":
            abn[0] = int(l[i*2+1])
            a = False
            if not b and not a:
                break
            else:
                abn[2] = 0
        elif b and l[i*2] == "B":
            abn[1] = int(l[i*2+1])
            b = False
            if not b and not a:
                break
            else:
                abn[2] = 1
    return abn

def moveTo(ab,abn):
    sec = 0
    
    mod = [1,1]
    if abn[0] < ab[0]:
        mod[0] = -1
    if abn[1] < ab[1]:
        mod[1] = -1
    
    
    si = abn[2]
#    print "mod",mod
#    print "si",si
#    print "ab",ab,"abn",abn
    
    while ab[si] != abn[si]:
        for i in range(2):
            if abn[i] != None:
                if ab[i] != abn[i]:
                    ab[i] += mod[i]
        sec += 1
    
#    print "push",si
    sec += 1
    
    o = 0
    if si == 0:
        o = 1
    
    if abn[o] != None:
        if ab[o] != abn[o]:
            ab[o] += mod[o]

    return ab,sec

for ln in range(t):
    l = file.readline().strip().split(" ")
    sn = int(l[0])
    l = l[1:]
    
    sec=0
    #a=O
    #b=B
    ab=[1,1]
    abn=[0,0,0]
    
    for step in range(sn):
        abn=findNext(step,l,sn)
        ab,s = moveTo(ab, abn)
        
        sec += s
    print "Case #%d:"%(ln+1),sec
#    break
#    print sn,l
file.close()
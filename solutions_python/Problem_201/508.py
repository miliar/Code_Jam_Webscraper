import collections,sys
#sys.stdin = open('input.in','r')
#sys.stdout = open('output.in','w')
t=int(input())
for u in range(t):
    n,k=map(int,input().split())
    tot = 1
    level  = 1
    i = 1
    while tot<k:
        i*=2
        tot+=i
        level+=1
    tot-=i
    d={}
    d[n] = 1
    i = 1
    while(i<level):
        i+=1
        _d={}
        for key in d:
            if(key%2==0):
                val1 = key//2
                val2 = key//2-1
                if(val1 in _d):
                    _d[val1]+=(d[key])
                else:
                    _d[val1]=(d[key])
                if(val2 in _d):
                    _d[val2]+=(d[key])
                else:
                    _d[val2]=(d[key])
            else:
                val = key//2
                if(val in _d):
                    _d[val]+=(2*d[key])
                else:
                    _d[val]=(2*d[key])
        d=_d
    tot=k-tot
    l = []
    for key in d:
        _l = []
        _l.append(key)
        _l.append(d[key])
        l.append(_l)
    l.sort(key=lambda x: x[0],reverse=True)
    for i in l:
        if(i[1]>=tot):
            if(i[0]%2==0):
                print("Case #"+str(u+1)+": "+str(i[0]//2)+" "+str(i[0]//2-1))
            else:
                print("Case #"+str(u+1)+": "+str(i[0]//2)+" "+str(i[0]//2))
            break
        else:
            tot-=i[1]

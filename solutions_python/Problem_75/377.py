t=int(raw_input())
for i in range(t):
    x=raw_input()
    x=x.split()
    c=int(x[0])
    combine=[]
    for j in range(c):
        combine.append(x[j+1])
    d=int(x[c+1])
    oppose=[]
    for j in range(d):
        oppose.append(x[c+j+2])
    n=int(x[c+d+2])
    string=x[c+d+3]
    x=[]
    x.append(string[0])
    for j in range(1,n):
        x.append(string[j])
        while True:
            flag=False
            for k in range(c):
                if len(x)<2:
                    break
                if (x[len(x)-1]==combine[k][0] and x[len(x)-2]==combine[k][1]) or (x[len(x)-1]==combine[k][1] and x[len(x)-2]==combine[k][0]):
                    flag=True
                    break
            if flag:
                x.pop()
                x.pop()
                x.append(combine[k][2])
            else:
                break
        flag=False
        for k in range(d):
            for l in range(len(x)-1):
                if (x[len(x)-1]==oppose[k][0] and x[l]==oppose[k][1]) or (x[len(x)-1]==oppose[k][1] and x[l]==oppose[k][0]):
                    x=[]
                    flag=True
                    break
            if flag:
                break
    s="Case #"
    s=s+str(i+1)
    s=s+": ["
    if len(x)>0:
        for j in range(len(x)-1):
            s=s+x[j]+", "
        s=s+x[len(x)-1]
    s=s+"]"
    print s
        
            

t=int(input())
for t in range(t):
    rt=input()
    rt=list(st)
    rt.reverse()
    print('Case #',end='')
    print(t+1,end=': ')
    for i in range(len(rt)-1):
        if(rt[i]>=rt[i+1]):
            continue
        else:
            rt[i+1]=str(int(rt[i+1])-1)
            for j in range(i+1):
                rt[j]='9'
        
    x=''.join(rt)
    #print(x)
    rt.reverse()
    rt=''.join(rt)
    print(int(rt))
            


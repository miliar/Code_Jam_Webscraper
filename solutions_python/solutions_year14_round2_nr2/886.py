def constantList(x):
    return x and [x[0]]*len(x) == x
n=int(input())
for j in range(n):
    t=int(input())
    a=[0 for i in range(t)]
    l=[0 for i in range(t)]
    for i in range(t):
        a[i]=str(input())
        l[i]=len(a[i])
    if(set(a[0])!=set(a[1])):
                 print('Case #'+str(j+1)+': Fegla Won')
    else:
                 print('Case #'+str(j+1)+': '+str((max(l)-min(l))))

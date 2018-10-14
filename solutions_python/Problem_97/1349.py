d = [[]]
for i in range(1, 2000001):
    nw = set()
    a = str(i)
    for j in range(len(a)):
        a=a[-1]+a[:-1]
        if (a[0]!='0' and int(a)>i):
            nw.add(int(a))
    d.append(list(nw))
    
def func(a, b):
    ans=0
    for i in range(a, b+1):
        for j in d[i]:
            if (j<=b):
                ans+=1
    return ans

inp=input('Data: ')
f=open(inp)
data = f.read().split('\n')
data = data[1:int(data[0])+1]
f.close()
f=open('a.out', 'w')
for i in range(len(data)):
    e = data[i].split(' ')
    f.write('Case #'+str(i+1)+': '+str(func(int(e[0]), int(e[1])))+'\n')
f.close()

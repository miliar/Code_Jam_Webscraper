def ispal(st):
    if len(st)<=1:
        return True
    else:
        return st[0]==st[-1] and ispal(st[1:-1])
a=[]
for i in range(1,10**7):
    if ispal(str(i)):
        if(ispal(str(i*i))):
            a.append(i*i)
            #print i*i
t=input()

for i in range(t):
    n,m=[int(x) for x in raw_input().split(' ')]
    c=0
    for u in a:
        if u >=n and u <= m:
            c+=1
    print "Case #"+str(i+1)+": "+str(c)

def tidy(n):
    while n>=0:
        a=str(n)
        for i in range(len(a)-1):
            if (int(a[i])>int(a[i+1])):
                break

        else:
            return n
        n=n-1
a=open('B-small-attempt2.in','r')
b=a.read().split('\n')
newf=open('def.in','w')
b.pop(0)
b.pop()
count=1
print b
for i in b:
    z=tidy(int(i))
    newf.write('Case #'+str(count)+':'+' '+str(z)+'\n')
    count+=1




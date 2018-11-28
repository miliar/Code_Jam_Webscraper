incoming=open('C-large.in','r')
a=int(incoming.readline())
f=open('C-large-output.txt','w')

for i in range(1,a+1):
    foo=incoming.readline()
    s=incoming.readline().split()
    a=[]

    testvalid = 0
    
    for x in s:
        y=int(x)
        testvalid^=y
        a.append(y)

    f.write("Case #"+str(i)+": ")
    
    if testvalid !=0:
        f.write("NO\n")
    else:
        f.write(str(sum(a)-min(a))+'\n')
f.close()
incoming.close()
        
        

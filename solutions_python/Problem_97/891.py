def getrecycle(A,x,B):
    m = []
    t = x
    for i in range(len(x)):
        t = t[len(x)-1]+t[:(len(x)-1)]
        if (x!=t and int(t)<=B and A<=int(t) and len(str(int(t)))==len(str(int(x)))):
            m.append(t)
    return(m)

def findnumber(A,B):
    n = A
    count = 0
    marked = []
    while n<B:
        if (str(n) in marked):
            n+=1
        else:
            m = getrecycle(A,str(n),B)
            count+=(((len(m)+1)*(len(m)))//2)
            marked.extend(m)
            n+=1
    return(count)

inp = open('C-small-attempt0.in','r')
outp = open('C-small-out.txt','w')

x = int(inp.readline())
i=1
while i<=x:
    a = (inp.readline()).strip().split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    outp.write('Case #'+str(i)+": "+str(findnumber(a[0],a[1]))+"\n")
    i+=1

inp.close()
outp.close()
            

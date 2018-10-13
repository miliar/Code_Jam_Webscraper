a = open('C-small-attempt0.in','r')
n = eval(a.readline().strip())

b = open('output.txt','w')


def fun(s):
    l = s.split()
    a = eval(l[0])
    b = eval(l[1])
    m = len(l[0])
    d = {}
    o = 0
    for i in range(a,b+1):
        k = str(i)
        
        p = 0
        for j in range(0,m-1):
            if eval(k[j+1]) != 0:
                t = k[j+1:] + k[0:j+1]
                if i < eval(t) and eval(t) <= b:
                    p = p + 1
        o = o + p
    return(o)
        
for i in range(1,n+1):
    s = a.readline().strip()
    b.write('Case #'+str(i)+': '+ str(fun(s))+'\n')


b.close()
a.close()



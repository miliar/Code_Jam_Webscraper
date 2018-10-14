def check(l):
    t=[]
    s=l.split(' ')
    cs=2
    c=float(s[0])
    f=float(s[1])
    x=float(s[2])
    tt=0
    t.append(x/cs)
    i=0
    while(True):
        tt+=float(c/cs)
        cs+=f
        t.append((x/cs)+tt)
        if(t[i]<t[i+1]):
            break
        i+=1
    return "%.6f"%t[i]
def test():
    data = open('bbb.txt','r')
    data2= open('bbb2.txt','w')
    k= data.read()
    line=k.split('\n')
    l=1
    c=line[1:]
    for j in range(int(line[0])):
        data2.write("Case #%d: %s\n" % (j+1,check(c[j])))
    data.close
    data2.close
test()

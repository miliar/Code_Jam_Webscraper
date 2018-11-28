def data(filename):
    fi = open(filename,'r')
    o = open(filename+".out",'w')
    tests = fi.readline().strip()
    a = fi.readlines()
    for i in range(0,int(tests)):
        c,f,x = map(float,a[i].strip().split())
        nf = 1
        t1 = x/2
        t2 = c/2+x/(2+nf*f)
        while (t1-t2 > 10**-7):
            nf += 1
            t1 = t2
            t2 = buy(c,f,nf) + x/(2+nf*f)
        o.write("Case #" + str(i+1) + ": %.7f\n" % t1)
    fi.close()
    o.close()
    
def buy(c,f,nf):
    time = 0
    for i in range(0,nf):
        time += c/(2+i*f)
    return time
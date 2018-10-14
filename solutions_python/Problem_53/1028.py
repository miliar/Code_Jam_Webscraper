#o=off no power
#f=off power
#n=on no power
#p=on power

def toggle(l):
    r = []
    for i in range(0,len(l)):
        if i==0:
            r.append(l[i]=='o' and 'p' or 'o')
        else:
            if r[i-1]=='p':
                if l[i]=='f':
                    r.append('p')
                if l[i]=='p':
                    r.append('f')
                if l[i]=='o':
                    r.append('f')
                if l[i]=='n':
                    r.append('p')
            else:
                if l[i]=='f':
                    r.append('n')
                if l[i]=='p':
                    r.append('o')
                if l[i]=='o':
                    r.append('o')
                if l[i]=='n':
                    r.append('n')

    return "".join(r)


f = open(r'C:\Users\flatline\development\gcode\A-small-attempt0.in')
lines = f.readlines()
f.close()

tst = lines[0]
ln = int(tst)+1

for i in range(1,ln):
    n,k = lines[i].split(' ')
    n,k = int(n),int(k)
    z = n
    f = "".ljust(z,'p')
    l = "".ljust(z,'o')
    p = l
    for kn in range(0,k):
        p = toggle(p)
    
    print 'Case #%s: %s'%(i,(p==f and 'ON' or 'OFF'))

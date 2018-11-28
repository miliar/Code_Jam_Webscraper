f = open("in.txt","r")
def nice(a,x):
    if a%x==0:
        return True
    if x%a==0:
        return True
    return False
import operator
out = open("out.txt","w")
cases = int(f.readline())
for case in xrange(1,cases+1):
    inc = f.readline().split()
    N = int(inc[0])
    L = int(inc[1])
    H = int(inc[2])
    mas = []
    mas = [int(x) for x in list(f.readline().split())]
    mas.sort()
    t = True
    for x in xrange(L,H+1):
        t = True
        for a in mas:
            if nice(x,a)==False:
                t = False
                break
        if t==True:
            out.write("Case #%d: %d\n"%(case,x))
            break
    if t!=True:out.write("Case #%d: NO\n"%case)
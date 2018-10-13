def minutes(p):
    p = p.split(':')
    return int(p[0].strip()) * 60 + int(p[1].strip())
def editsched(stime, fr, to, T):
    i = 0
    lf = len(fr)
    while i<lf and fr[i][0]<stime:
        i+=1
    if i<lf and not fr[i][0]<stime:
        nextt = fr[i][1] + T
        del fr[i]
        editsched(nextt, to, fr, T)

def dotestcase(casenr, f, g):
    T = int(f.readline())
    NN = f.readline().split()
    NA = int(NN[0])
    NB = int(NN[1])
    a, b, ra, rb = [], [], 0, 0
    for i in range(NA):
        data = f.readline().split()
        a.append((minutes(data[0]), minutes(data[1])))
    for i in range(NB):
        data = f.readline().split()
        b.append((minutes(data[0]), minutes(data[1])))
    a.sort()
    b.sort()
    while a or b:
        if not b:
            ra += len(a)
            a = []
        elif not a:
            rb += len(b)
            b = []
        else:
            if a[0]<b[0]:
                ra += 1
                editsched(0, a, b, T)
            else:
                rb += 1
                editsched(0, b, a, T)        
    g.write("Case #%d: %d %d\n"% (casenr, ra, rb))
    
        
f = open("input.txt")
g = open("output.txt", "w")

N = int(f.readline())
for i in range(N):
    dotestcase(i+1, f, g)
    

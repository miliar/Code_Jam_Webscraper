"""
Lawnmower
"""
def analyze_lawn(rows,n,m):
    bad = False
    cols = []
    for i in xrange(m):
        cols.append([x[i] for x in rows])
    for i in xrange(n):
        for j in xrange(m):
            test = rows[i][j]
            semibad = False
            for k in xrange(m):
                if(rows[i][k]>test):
                    semibad=True
                    break
            if(semibad):
                for k in xrange(n):
                    if(cols[j][k]>test):
                        return "NO"
    return "YES"

f = open("input2.txt", "rb")
g = open("output2.txt", "wb")
t = int(f.readline().strip())
for i in xrange(t):
    n,m = f.readline().strip().split()
    n,m = map(int,[n,m])
    lawn = []
    for j in xrange(n):
        lawn.append(f.readline().strip().split())
    g.write("Case #%d: %s" % (i+1, analyze_lawn(lawn,n,m)))
    g.write("\n")
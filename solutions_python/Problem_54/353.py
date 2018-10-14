
class Data():
    pass

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def solve(d):
    n = len(d.lis)
    a = []
    for i in range(n-1):
        a.append(abs(long(d.lis[i]) - long(d.lis[i+1])))
    v = a[0]
    for x in a:
        v = gcd(v, x)
    return (v - (long(d.lis[0]) % v)) % v
    
def readdata():
    global fin, fout
    nt = int(fin.readline())
    for testnum in range(1, nt+1):
        d = Data()
        d.lis = fin.readline().split()[1:]
        fout.write("Case #" + str(testnum) + ": " + str(solve(d)) + "\n")

def openfile(name):
    global fin, fout
    fin = open(name + ".in", 'r')
    fout = open(name + ".out", 'w')

def main(name):
    global fin, fout
    openfile(name)
    readdata()
    fin.close()
    fout.close()
    

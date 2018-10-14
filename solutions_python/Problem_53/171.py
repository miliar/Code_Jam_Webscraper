
class Data():
    pass

power = [2**k for k in range(30, -1, -1)]
def solve(d):
    k, n = d.k, d.n
    # Write k in binary
    b = []
    for p in power:
        if k >= p:
            b.append(1)
            k -= p
        else:
            b.append(0)
    for i in reversed(b):
        if i == 1:
            n -= 1
        else:
            break
    if n > 0:
        return "OFF"
    else:
        return "ON"
    
def readdata():
    global fin, fout
    nt = int(fin.readline())
    for testnum in range(1, nt+1):
        d = Data()
        n, k = fin.readline().split()
        d.n = int(n)
        d.k = int(k)
        fout.write("Case #" + str(testnum) + ": " + str(solve(d)) + "\n")

def openfile(name):
    global fin, fout
    if name[-3:] == ".in": name = name[:-3]
    fin = open(name + ".in", 'r')
    fout = open(name + ".out", 'w')

def main(name):
    global fin, fout
    openfile(name)
    readdata()
    fin.close()
    fout.close()
    

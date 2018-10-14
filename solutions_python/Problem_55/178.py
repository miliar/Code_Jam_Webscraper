# CodeJam!

class Data():
    pass

def solve(d):
    # For each i, find j max such that sum(i..j-1) <= k
    theJ = []
    priceGot = []
    for i in range(d.n):
        summan = 0
        j = i - 1
        while summan <= d.k and j < i + d.n:
            j += 1
            summan += d.g[j]
        theJ.append(j)
        priceGot.append(summan - d.g[j])
    #print theJ, priceGot
    now = 0
    ans = 0
    for i in range(d.r):
        ans += priceGot[now]
        now = theJ[now] % d.n
        #print ans, now
    return ans
    
def readdata():
    global fin, fout
    nt = int(fin.readline())
    for testnum in range(1, nt+1):
        d = Data()
        d.r, d.k, d.n = [int(x) for x in fin.readline().split()]
        d.g = [int(x) for x in fin.readline().split()]
        d.g = d.g*2
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
    

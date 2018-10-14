# Small & Large

def _ans(panks, max_size):
    ans = 0
    for pank in panks:
        ans += (pank-1)/max_size
    return ans + max_size

fin = open("largeB.txt", "r")
fout = open("largeB.out", "w+")

T = int(fin.readline())

for n in xrange(T):
    N = int(fin.readline())
    data = fin.readline().split()
    panks = []
    for i in xrange(N):
        panks.append(int(data[i]))

    ans = max(panks)
    for test in xrange(1, ans):
        tmp = _ans(panks, test)
        if tmp < ans:
            ans = tmp

    print "Case #%i: %i" %(n+1, ans)
    fout.write("Case #%i: %i\n" %(n+1, ans))
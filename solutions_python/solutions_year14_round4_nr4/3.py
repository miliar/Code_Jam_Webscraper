def reader(inFile):
    (M, N) = inFile.getInts()
    return (N, [inFile.readline() for i in xrange(M)])

from itertools import product

P = 1000000007

fcache = [1]
def fac(k):
    global fcache
    while k >= len(fcache):
        fcache += [fcache[-1] * len(fcache)]
    return fcache[k]

def comb(n,r):
    return fac(n)/(fac(r)*fac(n-r))

def score(num,nums):
    k = max(nums)
    tot = 0
    for i in xrange(k,num+1):
        val = comb(num,i)
        for j in nums:
            val = (val * comb(i,j)) % P
        tot += ((-1) ** (num + i)) * val
    return tot

def solver((N, words)):
    k = max([len(word) for word in words])
    wds = set(words)
    tot = 0
    record = {}
    followers = {}
    for i in xrange(k + 1):
        d = {}
        for w in words:
            if len(w) >= i:
                v = w[:i]
                if v in d:
                    d[v] += 1
                else:
                    d[v] = 1
        for v in d:
            scr = min(d[v],N)
            record[v] = scr
            if i > 0:
                prev = v[:-1]
                if prev in followers:
                    followers[prev] += [v]
                else:
                    followers[prev] = [v]
            tot += scr
    cnt = 1
    for v in followers:
        num = record[v]
        nums = [record[z] for z in followers[v]]
        if v in wds:
            nums += [1]
        cnt *= score(num,nums)
    cnt %= P
    while cnt >= P:
        cnt -= P
    while cnt < 0:
        cnt += P
    return "%d %d" % (tot, cnt)

if __name__ == "__main__":
    from GCJ import GCJ
    GCJ(reader, solver, "/Users/luke/gcj/2014/2/d/", "d").run()

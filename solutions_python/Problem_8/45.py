import math

def memoize(fn):
    mem = {}
    def mod(*args,**kwargs):
        key = hash((args,tuple([(k,kwargs[k]) for k in kwargs])))
        if mem.has_key(key):
            return  mem[key]
        else:
            val = fn(*args,**kwargs)
            mem[key] = val
            return val
    return mod

@memoize
def getPrimeFactors(nn):
    factors = []
    def factor(n):
        maxFactor = int(math.sqrt(n))
        for i in range(2,maxFactor+1):
            if n % i == 0:
                factors.append(i)
                factor(int(n/i))
                return
        factors.append(n)
    factor(nn)
    return factors



def func(A,B,P):
    itofactors = {}
    for i in range(A,B+1):
        itofactors[i] = set(getPrimeFactors(i))

    itoset = {}
    for i in range(A,B+1):
        itoset[i] = set([i])
    
    for i in range(A,B+1):
        for j in range(i,B+1):
            af = itofactors[i]
            bf = itofactors[j]
            inter = af & bf
            if len(inter) > 0:
                m = max(inter)
                if m >= P:
                    aset = itoset[i]
                    bset = itoset[j]
                    merge = aset | bset
                    for item in merge:
                        itoset[item] = merge
    ll = []
    for k in itoset:
        ll.append(tuple(list(itoset[k])))

    return len(set(ll))







if __name__ == "__main__":
    T = int(raw_input())
    for i in range(T):
        line = raw_input()
        line = line.split(' ')
        A = int(line[0])
        B = int(line[1])
        P = int(line[2])
        ans = func(A,B,P)
        print "Case #" + str(i+1) + ": " + str(ans)

import sys
from collections import defaultdict

def util_combine(combine):
    data = {}
    for c in combine:
        a = c[0]
        b = c[1]
        r = c[2]
        data[a + b] = data[b + a] = r
    return data

def util_opposed(opposed):
    data = defaultdict(str)
    for o in opposed:
        a = o[0]
        b = o[1]
        data[a] += b
        data[b] += a
    return data

def invoke(combine, opposed, chain):
    combine = util_combine(combine)
    opposed = util_opposed(opposed)
    
    alist = []
    counts = defaultdict(int)
    for el in chain:
        if alist:
            el0 = alist[-1]
            com = combine.get(el0 + el)
            if com is not None:
                alist[-1] = com
                counts[el0] -= 1
                continue
            reset = False
            for o in opposed[el]:
                if counts[o] > 0:
                    reset = True
                    break
            if reset:
                alist = []
                counts = defaultdict(int)
                continue
        alist.append(el)
        counts[el] += 1
    return alist
    
def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in range(1, T+1):
        data = f.readline().split()
        C = int(data.pop(0))
        combine, data = data[:C], data[C:]
        D = int(data.pop(0))
        opposed, data = data[:D], data[D:]
        data = data[1] # ignoring N
        
        alist = invoke(combine, opposed, data)
        print "Case #%d: [%s]" % (t, ', '.join(alist))

if __name__ == "__main__":
    main()
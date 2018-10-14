import sys

def permutations(n):
    s = str(n)
    
    ret = list()

    for i in range(len(s)):
        poss = int(s[i:] + s[:i])
        if poss not in ret:
            ret.append(poss)
            
    return ret


case = 1
for line in sys.stdin.readlines()[1:]:
    [a,b] = line.split(' ')
    a = int(a)
    b = int(b)

    count = 0
    found = dict()

    for n in range(a,b+1):
        for p in permutations(n):
            if p > n and p <= b:
                count += 1
                found[p] = True



    print "Case #%d: %d" % (case, count)
    case += 1

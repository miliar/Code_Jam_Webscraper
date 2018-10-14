#!/usr/bin/python

def solve(n):
    nlist = list(n)
    lastd = 0
    for i, d in enumerate(nlist):
        if d < lastd:
            break
        lastd = d
    else:
        return n
    
    for p in range(i, len(nlist)):
        nlist[p] = '9'

    carry = True
    p = i - 1
    while carry and p >= 0:
        d = int(nlist[p])
        if d == 0 or (p > 0 and int(nlist[p-1]) > d-1):
            nlist[p] = '9'
        else:
            carry = False
            nlist[p] = str(d - 1)
        p -= 1

    out = "".join(nlist)
    i = 0
    while out[i] == '0':
        i += 1
    return out[i:]

def main():
    t = int(raw_input())
    for i in xrange(t):
        n = raw_input()
        res = solve(n)
        print "Case #{}: {}".format(i + 1, res)

if __name__ == '__main__':
    main()

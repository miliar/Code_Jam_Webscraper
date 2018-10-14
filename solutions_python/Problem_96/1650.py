#! /usr/bin/env python
# coding:utf-8

tmap = {
 0: 0,
 1: 0,
 2: 0,
 3: 3,
 4: 3,
 5: 3,
 6: 6,
 7: 6,
 8: 6,
 9: 9,
 10: 9,
 11: 9,
 12: 12,
 13: 12,
 14: 12,
 15: 15,
 16: 15,
 17: 15,
 18: 18,
 19: 18,
 20: 18,
 21: 21,
 22: 21,
 23: 21,
 24: 24,
 25: 24,
 26: 24,
 27: 27,
 28: 27,
 29: 27,
 30: 30}

class s:
    def __init__(self, n):
        self.n = n
sp_num = s(0)
def canbig(p, bp):
    #print p, bp, sp_num.n
    if p < bp:
        return 0
    #mbase = tmap[p] / 3
    #ext = p - mbase * 3
    ##print mbase, ext
    #if mbase >= bp:
    #    return 1
    #if ext > 0 and mbase + 1 >= bp:
    #    return 1
    #if sp_num.n > 0 and mbase + 2 >= bp:
    #    sp_num.n -= 1
    #    return 1
    #return 0
    b = tmap[p] / 3
    e = p % 3
    if e == 0:
        if b >= bp:
            return 1
        elif sp_num.n > 0 and b > 0 and b + 1 >= bp:
            sp_num.n -= 1
            return 1
    elif e == 1:
        if b >= bp or b + 1 >= bp:
            return 1
        elif sp_num.n > 0 and b + 1 >= bp:
            sp_num.n -= 1
            return 1
    elif e == 2:
        if b >= bp or b + 1 >= bp:
            return 1
        elif sp_num.n > 0 and b + 2 >= bp:
            sp_num.n -= 1
            return 1
    return 0


def main():
    s = raw_input()
    n = int(s)
    ret = []
    for num in xrange(n):
        line = raw_input().split(" ")
        #gler_num = int(line[0])
        sp_num.n = int(line[1])
        base_point = int(line[2])
        ns = [int(i) for i in line[3:]]
        ret.append(sum([1 for i in ns if canbig(i, base_point)]))

    for n, i in enumerate(ret):
        print "Case #%d: %i" % (n+1, i)


if __name__ == "__main__":
    main()

import sys

DEBUG=True
DEBUG=False

def solve(n):
    if DEBUG: print "N: ", n
    blk_pos = 0
    check = True
    res = ""
    for i in xrange(1, len(n)):
        if check:
            if n[i-1] < n[i]:
                for j in xrange(blk_pos, i):
                    res += n[j]
                blk_pos = i
            elif n[i-1] > n[i]:
                check = False
                res += str(int(n[blk_pos]) - 1)
                for _ in xrange(blk_pos+1, i):
                    res += "9"
        else:
            res += "9"
    if check:
        for i in xrange(blk_pos, len(n)):
            res += n[i]
    else:
        res += "9"
    return int(res)

if __name__ == "__main__":
    i = 1
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        n = data.pop(0)
        print "Case #%d: %s" % (i, solve(n))
        i += 1

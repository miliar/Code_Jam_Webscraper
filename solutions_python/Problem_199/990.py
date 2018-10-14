#!/usr/bin/python

def flip(s):
    ret = ""
    for i in s:
        ret += ('-' if i == '+' else '+')
    return ret

def go(s, n):
    import pdb
    #pdb.set_trace()
    p = 0
    ret = 0
    while True:
        while p < len(s) and s[p] == '+': p += 1
        if p == len(s): return ret
        if p + n > len(s): return "IMPOSSIBLE"
        s[p : p + n] = flip(s[p : p + n])
        ret += 1


def main():
    N = int(raw_input())
    for i in xrange(N):
        s, n = raw_input().split(' ')
        print "Case #%d: %s" % (
            i + 1,
            go(list(s), int(n)),
        )

        
if __name__ == "__main__":
    main()

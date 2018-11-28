def ri():
    return int(raw_input().strip())

def rs():
    return raw_input().strip()

def lastt(s):
    l = 0
    for i in xrange(1, len(s)):
        if s[i] >= s[l]:
            l = i
        else:
            break
    return l

def ltidy(s):
    l = lastt(s)
    if l == len(s) - 1:
        return s
    while l < len(s) - 1:
        for i in xrange(l + 1, len(s)):
            s[i] = 9
        s[l] = (s[l] - 1) % 10
        l = lastt(s)
    return s

def toint(l):
    ret = 0
    for i in l:
        ret *= 10
        ret += i
    return ret

def main():
    t = ri()
    c = 1
    for n in xrange(t):
        s = [int(i) for i in rs()]
        print "Case #{}: {}".format(c, toint(ltidy(s)))
        c += 1
    
main()


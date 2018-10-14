def reduce_string(s):
    res = ""
    i = 0
    while i < len(s):
        res += s[i]
        while (i + 1) < len(s) and s[i] == s[i+1]:
            i += 1
        i += 1
    return res
        
def solve(ss):
    tmp = set(map(reduce_string, ss))
    if len(tmp) != 1:
        return "Fegla Won"
    orig = list(tmp)[0]
    def count(s):
        res = [0] * len(orig)
        idx = 0
        for i, o in enumerate(orig):
            while idx < len(s) and s[idx] == o:
                res[i] += 1
                idx += 1
        return res
    lengths = map(count, ss)
    ans = 0
    for i in xrange(len(orig)):
        mi = min(l[i] for l in lengths)
        ma = max(l[i] for l in lengths)
        ans += ma - mi
    return ans

for tc in xrange(1, input() + 1):
    N = input()    
    ss = [raw_input() for _ in xrange(N)]
    print "Case #{}: {}".format(tc, solve(ss))




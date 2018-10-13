def do_math(input):
    N, S, p = input[:3]
    scores = input[3:]
    res = 0
    for score in scores:
        avg, rest = divmod(score, 3)
        rest_pos = 1 if rest else 0
        if avg + rest_pos >= p:
            res += 1
        elif S > 0:
            if avg + rest >= p or (avg > 0 and avg + 1 >= p):
                S -= 1
                res += 1
    return res
    

T = int(raw_input())
for t in range(T):
    input = map(int, raw_input().split())
    print "Case #%d: %d" % (t + 1, do_math(input))

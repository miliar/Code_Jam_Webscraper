T = int(raw_input())

def prev_tidy_substract(n):
    i = 0
    rest = n
    diff = 0
    while rest >= 10:
        r = rest%10
        rest = rest/10
        diff += r * 10 ** i
        i+=1
        if r < rest%10:
            n -= (diff + 1)
            rest = n
            diff = 0
            i = 0
    return n

for i in range(T):
    N = int(raw_input())
    print "Case #%d: %d" % (i+1, prev_tidy_substract(N))

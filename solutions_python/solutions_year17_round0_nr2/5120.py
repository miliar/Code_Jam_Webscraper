T = int(raw_input())


def is_tidy(num):
    s = str(num)
    for i in xrange(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True


for case in range(T):
    N = int(raw_input())
    while True:
        if len(str(N))==1 or is_tidy(N):
            print "Case #%s: %s" % (case + 1, N)
            break
        N -= 1

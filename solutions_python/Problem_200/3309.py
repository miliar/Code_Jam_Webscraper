def get_largest_tidy_number(str_n):
    l = len(str_n)
    if l == 1:
        return str_n
    i = l - 1
    while i > 0:
        left = int(str_n[i-1])
        right = int(str_n[i])
        if(left > right):
            str_n = str_n[0:i-1] + str(left - 1) + (l - i) * "9"
        i -= 1
    return str_n.strip('0')

T = int(raw_input())
for i in xrange(1, T+1):
    N = raw_input()
    print "Case #%d: %s" % (i, get_largest_tidy_number(N))

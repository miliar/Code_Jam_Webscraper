def do_jam(input):
    n,k = input.split(' ')
    n = int(n)
    k = int(k)

    s = [n]

    l = 0
    r = 0
    for i in xrange(k):
        m = max(s)
        s.remove(m)
        r = (m-1)/2
        l = m/2
        s.append(l)
        s.append(r)


    return "{} {}".format(l,r)






########
# MAIN #
########
T= int(raw_input())
for i in xrange(1, T + 1):
    print "Case #{}: {}".format(i, str(do_jam(raw_input())))

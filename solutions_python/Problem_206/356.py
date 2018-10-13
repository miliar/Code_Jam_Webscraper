



def cruise(d, n, k, s):
    # first find the LAST horse to reach d
    last = 0
    for i in range(n):

        time = (d - k[i])/(s[i] + 0.0)
        last = max(last, time)

    # now we have the last horse - we want to reach D at that time too
    return (d + 0.0)/last

T = int(raw_input().strip())
for t in range(1, T+1):

    d, n = map(int, raw_input().strip().split(' '))
    k, s = [], []
    for _ in range(n):
        k_, s_ = map(int, raw_input().strip().split(' '))
        k.append(k_)
        s.append(s_)

    sol = cruise(d, n, k, s)
    print "Case #{}: {}".format(t, sol)

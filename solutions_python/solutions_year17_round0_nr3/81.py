import sys, math

toks = open(sys.argv[1], 'r').read().split()
toks.reverse()

T = int(toks.pop())
for t in xrange(T):
    N = int(toks.pop())
    K = int(toks.pop())

    conf = { N: 1 }
    nodes = 1

    while nodes < K:
        K -= nodes

        new_conf = {}
        for l, c in conf.iteritems():
            if l == 1:
                continue

            if l == 2:
                new_conf.setdefault(1, 0)
                new_conf[1] += c
                continue

            new_l = (l - 1) // 2

            new_conf.setdefault(new_l, 0)
            new_conf[new_l] += c
            if l % 2 == 1:
                new_conf[new_l] += c
            else:
                new_conf.setdefault(new_l+1, 0)
                new_conf[new_l+1] += c

        conf = new_conf
        nodes = sum(conf.itervalues())

    for node_len, node_count in sorted(conf.iteritems(), reverse=True):
        if node_count >= K:
            print 'Case #{}: {} {}'.format(t+1, int(math.ceil((node_len-1)/2.0)), int(math.floor((node_len-1)/2.0)))
            break
        K -= node_count

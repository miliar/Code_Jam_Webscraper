in_file = open('2a.in', 'r')

test_cases = int(in_file.readline())

ERR = 20000

def try_node(n, v):
    global nodes, memo

    a = memo.get('%s %s' % (n, v))
    if a: return a

    # constant
    try:
        if int(nodes[n-1]) == v:
            return 0
        else:
            return ERR
    except ValueError:
        pass

    t, c = [int(z) for z in nodes[n-1].split()]
    # t == 1: AND
    # t == 0: OR
    # c == changeable?

    if c == 0:
        if t == 1:
            # t == 1: AND
            if v == 0:
                a = try_node(n*2, 0)
                b = try_node(n*2+1, 0)

                c = try_node(n*2, 0)
                d = try_node(n*2+1, 1)

                e = try_node(n*2, 1)
                f = try_node(n*2+1, 0)

                r = min(a+b, c+d, e+f)

                if r>=ERR:
                    memo['%s %s' % (n, v)] = ERR
                    #print 'h1'
                    return ERR
                else:
                    memo['%s %s' % (n, v)] = r
                    #print 'h2'
                    return r

            else:
                a = try_node(n*2, 1)
                b = try_node(n*2+1, 1)
                if (a+b)>=ERR:
                    memo['%s %s' % (n, v)] = ERR
                    #print 'h3', a+b
                    return ERR
                else:
                    memo['%s %s' % (n, v)] = a + b
                    #print 'h4'
                    return a + b

        elif t == 0:
            # t == 0: OR
            if v == 0:
                a = try_node(n*2, 0)
                b = try_node(n*2+1, 0)

                if (a+b)>=ERR:
                    memo['%s %s' % (n, v)] = ERR
                    #print 'h5'
                    return ERR
                else:
                    memo['%s %s' % (n, v)] = a + b
                    #print 'h6'
                    return a + b

            else:
                a = try_node(n*2,   1)
                b = try_node(n*2+1, 0)

                c = try_node(n*2,   0)
                d = try_node(n*2+1, 1)

                e = try_node(n*2,   1)
                f = try_node(n*2+1, 1)

                r = min(a+b, c+d, e+f)
                if r >= ERR:
                    memo['%s %s' % (n, v)] = ERR
                    #print 'h7'
                    return ERR
                else:
                    memo['%s %s' % (n, v)] = r
                    #print 'h8', r
                    return r

    elif c == 1:
        if t == 1:
            # AND
            if v == 1:
                a = try_node(n*2, 1)
                b = try_node(n*2+1, 1)

                c = try_node(n*2, 0)
                d = try_node(n*2+1, 1)

                e = try_node(n*2, 1)
                f = try_node(n*2+1, 0)

                r = min(a+b, c+d+1, e+f+1)
                if r >= ERR:
                    memo['%s %s' % (n, v)] = ERR
                    #print 'h9', r
                    return ERR
                else:
                    memo['%s %s' % (n, v)] = r
                    #print 'h10', r
                    return r

            else:
                a = try_node(n*2, 0)
                b = try_node(n*2+1, 0)

                c = try_node(n*2, 0)
                d = try_node(n*2+1, 1)

                e = try_node(n*2, 1)
                f = try_node(n*2+1, 0)

                #print a, b, c, d, e, f
                r = min(a+b, c+d, e+f)
                if r >= ERR:
                    memo['%s %s' % (n, v)] = ERR
                    #print 'h9a', r
                    return ERR
                else:
                    memo['%s %s' % (n, v)] = r
                    #print 'h10a', r
                    return r

        else:
            # OR
            if v == 1:
                a = try_node(n*2, 1)
                b = try_node(n*2+1, 1)

                c = try_node(n*2, 0)
                d = try_node(n*2+1, 1)

                e = try_node(n*2, 1)
                f = try_node(n*2+1, 0)

                r = min(a+b, c+d, e+f)
                if r >= ERR:
                    memo['%s %s' % (n, v)] = ERR
                    #print 'h11'
                    return ERR
                else:
                    memo['%s %s' % (n, v)] = r
                    #print 'h12'
                    return r

            else:
                a = try_node(n*2, 0)
                b = try_node(n*2+1, 0)

                c = try_node(n*2, 0)
                d = try_node(n*2+1, 1)

                e = try_node(n*2, 1)
                f = try_node(n*2+1, 0)

                r = min(a+b, c+d+1, e+f+1)
                if r >= ERR:
                    memo['%s %s' % (n, v)] = ERR
                    #print 'h11a'
                    return ERR
                else:
                    memo['%s %s' % (n, v)] = r
                    #print 'h12a'
                    return r


for t in range(1, test_cases+1):
    global nodes, memo
    M, V = [int(v) for v in in_file.readline().split()]
    nodes = []
    memo = {}
    for m in range(M): nodes.append(in_file.readline())

    r = try_node(1, V)

    if r == ERR: r = 'IMPOSSIBLE'

    print 'Case #%d: %s' % (t, r)

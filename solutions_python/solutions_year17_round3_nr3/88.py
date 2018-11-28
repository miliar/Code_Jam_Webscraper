import sys

def next_line():
    return input_file.readline().rstrip()

input_file = open(sys.argv[1])
for case in range(1, int(next_line())+1):
    print "Case #%s:" % (case),
    N, K = map(int, next_line().split())
    U = float(next_line())
    prob = map(float, next_line().split())
    prob += [1.0]
    prob.sort()
    #print prob, U
    for i, p in enumerate(prob):
        if sum(p-pi for pi in prob[:i]) > U:
            #x*(i-1) + sum(-pi for pi in prob[:i]) == U
            #x == (U - sum(-pi for pi in prob[:i])) / (i-1)
            #x == (U + sum(pi for pi in prob[:i])) / (i-1)
            x = (U + sum(pi for pi in prob[:i])) / i
            assert(abs(sum(x-pi for pi in prob[:i]) - U) < 1e-8)
            prod = 1
            for pr in reversed(prob[i:]):
                prod *= pr
            for pr in reversed(prob[:i]):
                prod *= x
            print prod
            break
        elif p == 1:
            print 1.0
            break
    else:
        print 1.0

T = int(raw_input())

for t in range(T):
    C, F, X = [float(x) for x in raw_input().split()]
    curr_f = 2.
    curr_t = 0.
    while X / curr_f > (C / curr_f + X / (curr_f + F)):
        curr_t += C / curr_f
        curr_f += F

    res = curr_t + X / curr_f
    print 'Case #{}: {:.7f}'.format(t+1, res)

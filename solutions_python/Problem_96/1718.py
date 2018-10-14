#!/usr/bin/python3

def best(n):
    return (n + 2) // 3

def max_surp(n):
    return (n + 4) // 3


T = int(input())
for t in range(T):
    N, S, p, *totals = map(int, input().split())

    got_at_least_p  = sum(1 for total in totals if best(total) >= p)
    could_have_got_p_if_surprised = sum(1 for total in totals
                                        if best(total) == p - 1 and
                                           total % 3 != 1 and
                                           2 <= total <= 28)

#    print()
#    print('got:', got_at_least_p)
#    print('could:', could_have_got_p_if_surprised)
#    print('s:', S)

    m = got_at_least_p + min(could_have_got_p_if_surprised, S)

    print('Case #{}: {}'.format(t + 1, m))


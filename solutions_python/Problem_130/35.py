def max_num_losses(i, N, P):
    n_better = i
    max_losses = 0
    while n_better > 0:
        max_losses += 1
        n_better = (n_better - 1) / 2
    return max_losses


def max_num_wins(i, N, P):
    n_worse = 2 ** N - i - 1
    max_wins = 0
    while n_worse > 0:
        max_wins += 1
        n_worse = (n_worse - 1) / 2
    return max_wins


def team_could_win(i, N, P):
    max_wins = max_num_wins(i, N, P)
    min_losses = N - max_wins
    best_rank = 2 ** min_losses
    return best_rank <= P


def team_could_loose(i, N, P):
    max_losses = max_num_losses(i, N, P)
    min_wins = N - max_losses
    worst_rank = 2 ** N - 2 ** min_wins + 1
    return worst_rank > P


def lowest_team_that_could_win(N, P):
    low = 0
    high = 2 ** N - 1
    while high - low > 1:
        mid = (high + low) / 2
        if team_could_win(mid, N, P):
            low = mid
        else:
            high = mid
    left = high - low + 1
    assert left == 1 or left == 2
    assert team_could_win(low, N, P)
    assert high == 2 ** N - 1 or not team_could_win(high+1, N, P)
    # print 'low = %d, high = %d' % (low, high)
    if left == 2 and team_could_win(high, N, P):
        return high
    else:
        return low


    # for i in reversed(range(2**N)):
    #     if team_could_win(i, N, P):
    #         return i


def highest_team_that_could_loose(N, P):
    low = 0
    high = 2 ** N - 1
    while high - low > 1:
        mid = (high + low) / 2
        if team_could_loose(mid, N, P):
            high = mid
        else:
            low = mid
    left = high - low + 1
    if left == 2 and team_could_loose(low, N, P):
        return low
    elif team_could_loose(high, N, P):
        return high
    else:
        return high + 1

    # for i in range(2 ** N):
    #     if team_could_loose(i, N, P):
    #         return i
    # return 2 ** N


def solve(N, P):
    n_t = 2 ** N
    return highest_team_that_could_loose(N, P) - 1, lowest_team_that_could_win(N, P)


##############################################################################

def read_ints(f):
    s = f.readline()
    return [int(w) for w in s.strip().split()]


from sys import argv

in_fn = argv[1]
out_fn = len(argv) > 2 and argv[2] or in_fn + '.out'

in_f = open(in_fn)
out_f = open(out_fn, 'w')

T = int(in_f.readline().strip())

for i_t in range(T):
    # cache = {}
    N, P = read_ints(in_f)
    res = solve(N, P)
    out_ln =  'Case #%d: %s %s' % (i_t+1, res[0], res[1])
    print >> out_f, out_ln
    print out_ln




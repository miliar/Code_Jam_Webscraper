# Google Code Jam : Qualification Round 2011 : Problem A. Bot Trust
# https://code.google.com/codejam/contest/dashboard?c=975485#s=p0
# Python 2.6.5

def seconds_required(seq):
    T = 0
    To = 0
    Tb = 0
    op = 1
    bp = 1

    for c in seq:

        if c[0] == "O":
            T = max(T + 1, To + abs(c[1] - op) + 1)
            To = T
            op = c[1]

            #print "O", T, To

        else:
            T = max(T + 1, Tb + abs(c[1] - bp) + 1)
            Tb = T
            bp = c[1]

            #print "B", T, Tb

    return T


def solve_case(t, seq_str):
    pre_seq = seq_str.split()[1:]
    i = iter(pre_seq)
    seq = zip(i, i)
    for i in range(0, len(seq)):
        seq[i] = (seq[i][0], int(seq[i][1]))
    print "Case #" + str(t) + ": " + str(seconds_required(seq))

def solve():
    T = int(raw_input())
    for t in range(1, T + 1):
        solve_case(t, raw_input())

solve()

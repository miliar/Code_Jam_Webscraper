import sys

__author__ = 'joranvar'

def solve(case):
    N, S, p = case[0:3]
    total_scores = case[3:]

    # No surprise needed if the total score >= 3p - 2 where p >= 1
    # Surprise needed if the total score is 3p - 4 or 3p - 3 where p >= 2
    # Otherwise no hit

    no_surprise, surprise = 0,0
    for score in total_scores:
        if score >= 3*p - 2:
            no_surprise += 1
        elif score >= 3*p - 4 and p >= 2:
            surprise += 1

    return str(no_surprise + min(S, surprise)) + '\n'

if __name__ == "__main__":
    fi = open('b.in')

    T = int(fi.readline())
    cases = [list(map(int, l.split(' '))) for l in fi.readlines()]

    G = [s for s in map(solve, cases)]

    fo = open('b.out', 'w')
    fo.writelines(['Case #' + str(i) + ': ' + l for i, l in enumerate(G,1)])

    fo.flush()
    fo.close()
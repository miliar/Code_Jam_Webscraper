
def solve(N, S, p, scores):
    scores.sort(reverse=True);
    res = 0
    for score in scores:
        if score >= 3*p - 2:
            res += 1
        elif max(2, 3*p - 4) <= score and S > 0:
            res += 1
            S -= 1
    return res



n = int(raw_input())

for i in range(n):
    tab = map(int, raw_input().split(' '))
    print "Case #" + str(i+1) + ": " + str(solve(tab[0], tab[1], tab[2], tab[3:]))



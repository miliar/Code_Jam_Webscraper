import sys

MAT = {
    9: ([4,5], [3,3,3]),
    8: ([4,4], [2,3,3]),
    7: ([3,4], [2,2,3]),
    6: ([3,3], [2,2,2]),
    5: ([2,3], [1,2,2]),
    4: ([2,2], ),
}

def solve(P):
    if len(P) == 0:
        return 0

    if P[-1] == 1:
        return 1
    if P[-1] == 2:
        return 2
    if P[-1] == 3:
        return 3

    m = P.pop()
    score = m

    for rest in MAT[m]:
        assert sum(rest) == m
        score = min(score, len(rest)-1 + solve(sorted(P + rest)))
    return score

for case_no in xrange(1, input() + 1):
    print >> sys.stderr, "Case #%s:" % (case_no,)
    print "Case #%s:" % (case_no,),

    _ = input()
    P = sorted(map(int, raw_input().split()))
    print solve(P)




#     1     2
# 9  4+5  3+3+3
# 8  4+4  2+2+3

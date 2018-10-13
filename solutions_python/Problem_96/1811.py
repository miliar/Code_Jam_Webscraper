def check_score(scores, p):
    if scores:
        for s in scores:
            if s >= p:
                return True
    return False

def calc_score(total, pattern):
    scores = [0, 0, 0]
    x = (total - sum(pattern)) / 3
    for i in range(0, len(pattern)):
        scores[i] = x + pattern[i]
    if sum(scores) == total and min(scores) >= 0:
        return scores
    else:
        return None

def isPossible(total, p, patterns):
    for pattern in patterns:
        scores = calc_score(total, pattern)
        if check_score(scores, p):
            return True
    return False

def surprising(total, p):
    patterns = [ [2, 1, 0], [2, 2, 0], [2, 0, 0] ]
    if isPossible(total, p, patterns):
        return 1
    else:
        return 0

def non_surprising(total, p):
    patterns = [ [1, 0, 0], [1, 1, 0], [0, 0, 0] ]
    if isPossible(total, p, patterns):
        return 1
    else:
        return 0

def _solve(s, p, totals, i):
    if i < len(totals):
        s_result = 0
        if s > 0:
            s_result = surprising(totals[i], p)
            s_result = s_result + _solve(s - 1, p, totals, i + 1)

        n_result = 0
        if s != len(totals) - i:
            n_result = non_surprising(totals[i], p)
            n_result = n_result + _solve(s, p, totals, i + 1)

        return max(s_result, n_result)
    else:
        return 0

def solve(s, p, totals):
    return _solve(s, p, totals, 0)

import sys
numCases = int(sys.stdin.readline())
for i in range(1, numCases + 1):
    input = list(sys.stdin.readline().rstrip().split())
    num_players = int(input[0])
    s = int(input[1])
    p = int(input[2])
    totals = []
    for j in range(0, num_players):
        totals.append(int(input[j + 3]))
    print "Case #" + str(i) + ": " + str(solve(s, p, totals))
    

#!/usr/bin/python

def read_text():
    data = [int(v) for v in raw_input().split(" ")]
    n, s, p = data[0], data[1], data[2]
    scores = data[3:]
    return n, s, p, scores

def get_score(score, r):
    for i in r:
        lscore = score + i
        if lscore % 3 == 0:
            return lscore / 3
    return None

def max_score_supr(score):
    if score < 2:
        return None
    return get_score(score, range(2, 5));

def max_score(score):
    return get_score(score, range(0, 3));

def solve(n, s, p, scores):
    m = 0
    for i in scores:
        supr = max_score_supr(i)
        norm = max_score(i)
        if norm >= p:
            m += 1
        elif supr != None and supr >= p and s > 0:
            m += 1
            s -= 1
    return m

t = int(raw_input())
k = 1
for i in range(t):
    n, s, p, scores = read_text()
    print "Case #%d: %d" % (k, solve(n, s, p, scores))
    k += 1

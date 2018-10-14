from collections import deque

def real_war(p1, p2):
    """
    p1 plays first. Strategy is to always play the biggest.
    p2 will play a bigger one if possible (smallest bigger but doesn't matter)
    and if not the smallest one
    """
    score = 0
    for _ in xrange(len(p1)):
        m1 = p1.pop()
        m2 = p2.pop()
        if m2 < m1:
            p2.append(m2)
            p2.popleft()
            score += 1
    return score

def cheating_war(p1, p2):
    """
    p1 plays first. Strategy is to play smallest number that can win and claim
    its value is higher than max. That way player 2 will choose lowest
    """
    score = 0
    for item in p1:
        if item > p2[score]:
            score+=1
    return score

T = input()
for i in xrange(T):
    print "Case #%d:" % (i + 1),
    _ = raw_input()
    p1 = map(float, raw_input().split())
    p1.sort()
    p1 = deque(p1)
    p2 = map(float, raw_input().split())
    p2.sort()
    p2 = deque(p2)
    print cheating_war(p1, p2), real_war(p1, p2)

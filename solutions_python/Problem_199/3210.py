#!/usr/bin/env python
import time

def allHappy(s):
    #print "%s : %s" % (s, target)
    return s == target

def flip(c):
     if c == "+":
         return "-"
     else:
         return "+"

def available_moves(s):
    i = 0
    #print s
    while i <= len(s) - K:
        m = s[0:i] + ''.join([flip(x) for x in s[i:i+K]])+ s[i+K:]
        #print "%s%s%s" % (s[0:i], ''.join([flip(x) for x in s[i:i+K]]), s[i+K:])
        yield m
        i += 1

def solve():
    #print "Solving %s with K=%d" % (S, K)

    if allHappy(S):
        return 0

    visited = {}
    visited[S] = 0
    stack = []
    stack.append((S, 0))
    while len(stack) > 0:
        s, steps = stack.pop()
        #print "%s\t%d" % (s, steps)
        for nm in available_moves(s):
            nextStep = steps + 1
            #print "%s\t%d" % (nm, nextStep)
            #print visited
            #print stack
            if not nm in visited or nextStep < visited[nm]:
                visited[nm] = nextStep
                stack.append((nm, nextStep))

    return visited.get(target, "IMPOSSIBLE")

T = input()
for i in range(1, T + 1):
    fields = raw_input().split()
    S = fields[0]
    K = int(fields[1])
    target = len(S) * "+"
    times = solve()
    print "Case #%d: %s" % (i, times)

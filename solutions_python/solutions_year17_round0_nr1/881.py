#!/usr/bin/python


def readfile():
    pancakes = []
    with open('pancakes.in', 'r') as f:
        n = int(f.readline())
        for line in f:
            row, flipper = line.split()
            flipper = int(flipper)
            pancakes.append((row, flipper))
    return pancakes

'''
def solve(s, k):
    from collections import deque
    visited = set([])
    q = deque([list(s)])
    c = 0
    n = len(s)
    found = False
    nextlevel = []
    while q or nextlevel:
        if not q:
            q.extend(nextlevel)
            c += 1
            nextlevel = []
        state = q.popleft()
        if '-' not in state:
            found = True
            break
        for i in xrange(n-k+1):
            newstate = state[:]
            for j in xrange(i, i+k):
                newstate[j] = '+' if newstate[j] == '-' else '-'
            if ''.join(newstate) not in visited:
                visited.add(''.join(newstate))
                nextlevel.append(newstate)
    return found, c
'''
	

def solve(s, k):
	s = list(s)
	c = 0
	for i in xrange(len(s)-k+1):
		if s[i] == '-':
			c += 1
			for j in xrange(i, i+k):
				s[j] = '+' if s[j] == '-' else '-'
	return not '-' in s, c


pancakes = readfile()
with open('pancakes.out', 'w') as f:
    for i, pancake in enumerate(pancakes):
        found, c = solve(pancake[0], pancake[1])
        c = str(c) if found else 'IMPOSSIBLE'
        newline = '\n' if i < len(pancakes) else ''
        f.write('Case #%d: %s%s' % (i+1, c, newline))


import sys

def solve(state, k):
    pancakes = [1 if c == '+' else 0 for c in state]
    def flip(idx):
        assert 0 <= idx < len(pancakes)
        for i in range(idx, idx+k):
            pancakes[i] = 1 - pancakes[i]

    flips = 0
    for i in range(len(pancakes) - k + 1):
        if pancakes[i] == 0:
            flips += 1
            flip(i)

    if all(p == 1 for p in pancakes):
        print flips

    else:
        print "IMPOSSIBLE"

lines = sys.stdin.readlines()
for i, l in enumerate(lines[1:]):
    state, k = l.strip().split(' ')
    print "Case #%d: " % (i+1),
    solve(state, int(k))

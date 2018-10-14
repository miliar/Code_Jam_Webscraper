T = int(raw_input().strip())

def flip(state, pos, k):
    for p in range(pos, pos + k):
        state[p] = '+' if state[p] == '-' else '-'

for t in range(1, T + 1):
    state, k = raw_input().strip().split()
    state = list(state)
    k = int(k)
    flips = 0
    solved = False
    for pos in range(len(state) - k + 1):
        if state[pos] == '-':
            flip(state, pos, k)
            flips += 1

        if set(state) <= {'+'}:
            solved = True
            print 'Case #%d: %d' % (t, flips)
            break
    if not solved:
        print 'Case #%d: IMPOSSIBLE' % (t)


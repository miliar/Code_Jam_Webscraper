def solve(state, k):
    num_flips = 0
    idx = 0
    while idx + k <= len(state):
        if state[idx] == '+':
            idx += 1
            continue
        for curr in xrange(idx, idx + k):
            if state[curr] == '+':
                state[curr] = '-'
            else:
                state[curr] = '+'
        idx += 1
        num_flips += 1
    if '-' in state:
        return "IMPOSSIBLE"
    else:
        return str(num_flips)

num_cases = int(raw_input())
for case in xrange(1, 1 + num_cases):
    raw = raw_input()
    problem = raw.split()
    print "Case #" + str(case) + ": " + solve(list(problem[0]), int(problem[1]))

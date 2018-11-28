import sys

def solve_case(state):
    state.sort()

    minutes = 0
    
    inert_attempt = max(state)

    if inert_attempt <= 2:
        return inert_attempt

    return min(inert_attempt, twoway(state), threeway(state))

def twoway(s):
    state = [x for x in s if x > 0]
    max_s = max(state)
    to_append = []
    for i, s in enumerate(state):
        if s == max_s:
            state[i] = max_s / 2
            to_append.append(max_s - max_s / 2)
    state.extend(to_append)
    return solve_case(state) + len(to_append)

def threeway(s):
    state = [x for x in s if x > 0]
    max_s = max(state)
    to_append = []
    for i, s in enumerate(state):
        if s == max_s:
            state[i] = max_s / 3
            to_append.append(max_s - max_s / 3)
    state.extend(to_append)
    return solve_case(state) + len(to_append)


lines = sys.stdin.readlines()

testcases = int(lines[0])

lines = lines[2::2]
lines = [l.rstrip() for l in lines]

results = []

for i in range(testcases):
    results.append(solve_case([int(x) for x in lines[i].split(" ")]))

for i, r in enumerate(results, start = 1):
    print ("Case #%d: %d" % (i, r))


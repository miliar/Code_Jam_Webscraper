def solve(state, k):
    i = 0
    flips = 0
    while i < len(state):
        #print i, state
        if state[i] == '-':
            for j in range(i, i+k):
                if j >= len(state):
                    return "IMPOSSIBLE"
                elif state[j] == '-':
                    state[j] = '+'
                elif state[j] == '+':
                    state[j] = '-'
            flips += 1
        i += 1
    return str(flips)

num_cases = input()
for i in range(num_cases):
    state, k = raw_input().split(" ")
    k = int(k)
    print "Case #%d: %s" % (i+1, solve(list(state), k))

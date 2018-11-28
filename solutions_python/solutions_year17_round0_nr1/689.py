import sys
inp = sys.stdin.readlines()

cases = int(inp.pop(0))

for case in range(1, cases + 1):
    line = inp.pop(0).strip()
    S, K = line.split()
    K = int(K)
    count = 0
    diff = [S[0] == '-'] + [S[i] != S[i+1] for i in range(len(S)-1)] + [False]
    for i in range(len(S) - K + 1):
        if diff[i]:
            diff[i+K] = not diff[i+K]
            count += 1
    result = "IMPOSSIBLE" if any(diff[len(S) - K + 1:len(S)]) else count
    print 'Case #{}: {}'.format(case, result)

def flip(S, K, i):
    flipped = ''.join([('-' if cake == '+' else '+') for cake in S[i:i + K]])
    return S[:i] + flipped + S[i + K:]


def solve(S, K):
    answer = 0
    for i in range(len(S) - K + 1):
        if S[i] == "-":
            S = flip(S, K, i)
            answer += 1
    return 'IMPOSSIBLE' if any(i != '+' for i in S) else answer


with open("A-large.in", "r") as f:
    file = f.readlines()
    T = int(file.pop(0))
    for t in range(T):
        line = file.pop(0).strip().split(' ')
        S = line[0]
        K = int(line[1])
        print "Case #%d: %s" % (t + 1, solve(S, K))

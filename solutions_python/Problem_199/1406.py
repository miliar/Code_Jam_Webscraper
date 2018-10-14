import sys

filename = sys.argv[1]
f = open(filename)
T = int(f.readline())


def flip(i, S, K):
    for k in range(K):
        c = S[i + k]
        if c == "+":
            S[i + k] = "-"
        else:
            S[i + k] = "+"
    

def solve(S, K):
    count = 0
    
    for i, s in enumerate(S):
        if s == '+':
            continue
        elif i > len(S) - K:
            break
        else:
            flip(i, S, K)
            count += 1

    for s in S:
        if s == '-':
            return 'IMPOSSIBLE'
    return count


for t in range(T):
    S, K = f.readline().strip().split()
    K = int(K)
    S = list(S)
    answer = solve(S, K)

    print "Case #{}: {}".format(t + 1, answer)

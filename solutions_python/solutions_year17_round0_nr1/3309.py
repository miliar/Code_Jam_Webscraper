def solve(S, K, curIdx, acc):
    while curIdx < len(S) and S[curIdx] == '+':
        curIdx += 1
    if curIdx == len(S):
        return acc
    if len(S) - curIdx < K:
        return 'IMPOSSIBLE'
    # flip pancakes
    for i in range(curIdx, curIdx + K):
        S[i] = '-' if S[i] == '+' else '+'
    return solve(S, K, curIdx, acc + 1)

if __name__ == "__main__":
    inputs = open('./A-small.in.txt')
    outputs = open('./A-small.out.txt', 'w')
    # inputs = open('./A-large.in.txt')
    # outputs = open('./A-large.out.txt', 'w')
    T = int(inputs.readline())
    for c in range(1, T + 1):
        S, K = inputs.readline().split()
        # format inputs
        S = list(S)
        K = int(K)
        sol = solve(S, K, 0, 0)
        outputs.write("Case #{0}: {1}\n".format(c, sol))
    inputs.close()
    outputs.close()



def oversized_pancake_flipper(S, K):
    assert 2 <= K <= len(S)
    S = list(S)
    times = 0
    for i in range(len(S) + 1 - K):
        if S[i] == '-':
            times += 1
            for j in range(K):
                S[i + j] = '+' if S[i + j] == '-' else '-'

    if all(c is "+" for c in S):
        return times
    else:
        return "IMPOSSIBLE"

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S, K = input().split()
        print("Case #{}: {}".format(i + 1, oversized_pancake_flipper(S.strip(), int(K))))


def do(S, K):
    count = 0
    for i in range(len(S)):
        if i + K > len(S):
            break

        flipped = ''

        if S[i] == '-':
            count += 1
            j = 0
            while j < len(S):
                if i == j:
                    for k in range(K):
                        flipped += '+' if S[j] == '-' else '-'
                        j += 1
                try:
                    flipped += '-' if S[j] == '-' else '+'
                except Exception as e:
                    break

                j += 1

            S = flipped

    return count if '-' not in S else 'IMPOSSIBLE'

if __name__ == '__main__':
    T = int(input())
    for i in range(1, T + 1):
        S, K = input().split()
        K = int(K)
        r = do(S, K)
        print("Case #{}: {}".format(i, r))

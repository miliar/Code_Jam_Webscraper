def main():
    T = int(input())
    for i in range(T):
        S, K = input().split()
        S = [s for s in S]
        K = int(K)
        count = 0
        for j in range(len(S)-K+1):
            s = S[j]
            if s == '-':
                for k in range(K):
                    ss = S[j+k]
                    if ss == '+':
                        S[j+k] = '-'
                    elif ss == '-':
                        S[j+k] = '+'
                count += 1

        possibility = True
        for s in S[-K+1:]:
            if s == '-':
                possibility = False
                break

        if possibility:
            print('Case #{}: {}'.format(i+1, count))
        else:
            print('Case #{}: IMPOSSIBLE'.format(i+1))

if __name__ == '__main__':
    main()

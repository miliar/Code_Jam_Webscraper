def main():
    T = int(input().strip())

    for t in range(T):
        S, K = input().strip().split()
        S, K = list(S), int(K)

        y = 0
        for i in range(len(S)- K + 1):
            if S[i] is '-':
                S[i:i+K] = map(lambda c: chr(ord(c)^6), S[i:i+K])
                y += 1
        print('Case #{}: {}'.format(t+1, 'IMPOSSIBLE' if '-' in S else y))

if __name__ == '__main__':
    main()

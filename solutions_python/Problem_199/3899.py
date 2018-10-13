def spam(text, K):
    for i in range(K):
        for j in range(len(text) - K + 1):
            t = text[j: j + K]
            if t[: K - i] == '-' * (K - i):
                return text[: j] + t.replace('+', '*').replace('-', '+').replace('*', '-') + text[j + K:]
    return ''


def main():
    with open('A-small-attempt1.in') as f:
        T = int(f.readline()[:-1])
        for i in range(T):
            S, K = f.readline()[:-1].split()
            K = int(K)

            ans = 0
            text = S
            while True:
                text = text.strip('+')

                if len(text) == 0:
                    print('Case #{0}: {1}'.format(i + 1, ans))
                    break

                if len(text) < K:
                    print('Case #{0}: {1}'.format(i + 1, 'IMPOSSIBLE'))
                    break

                text = spam(text, K)
                if not text:
                    print('Case #{0}: {1}'.format(i + 1, 'IMPOSSIBLE'))
                    break

                ans += 1


if __name__ == '__main__':
    main()

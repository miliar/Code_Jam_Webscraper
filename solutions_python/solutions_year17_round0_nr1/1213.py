'''
Oversized Pancake Flipper
'''


def main():
    t = int(input())
    for x in range(1, t + 1):
        y = 0
        S, K = input().split()
        K = int(K)
        # happyside = '+' * K
        # blankside = '-' * K
        S = S.strip('+')
        while len(S) >= K:
            if S[0] == '-':
                flipped = ''.join('+' if x == '-' else '-' for x in S[:K])
                S = flipped + S[K:]
            y += 1
            S = S.strip('+')
        if S:
            y = 'IMPOSSIBLE'
        print ("Case #{}: {}".format(x, y))


if __name__ == '__main__':
    main()

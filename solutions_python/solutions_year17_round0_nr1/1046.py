def flip(c):
    if c == '-': return '+'
    else: return '-'

def solve(S, K):
    """ solve the problem """

    S = list(S)
    count = 0
    for i in range(len(S)):
        if S[i] == '-':
            if i+K>len(S): return 'IMPOSSIBLE'
            else:
                count += 1
                for j in range(i, i+K):
                    S[j] = flip(S[j])

    return count


def parse():
    """ parse input """
    S, K = input().split()
    K = int(K)

    return S, K


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()

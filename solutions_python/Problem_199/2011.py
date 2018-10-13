import sys


def solve(S, K):
    if '-' not in S:
        return 0

    cnt = 0
    while '-' in S:
        idx = S.index('-')
        if idx + K > len(S):
            return 'IMPOSSIBLE'

        for i in range(idx, idx + K):
            if S[i] == '+':
                S[i] = '-'
            else:
                S[i] = '+'
        cnt += 1

    return cnt


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        src = f.read()

    lines = src.splitlines()
    T = int(lines.pop(0))

    result = ''
    for i in range(T):
        S, K = lines.pop(0).split(maxsplit=1)
        result += 'Case #{idx}: {result}\n'.format(idx=i+1, result=solve(list(S), int(K)))

    #print(result)
    with open('output.txt', 'w') as f:
        f.write(result)

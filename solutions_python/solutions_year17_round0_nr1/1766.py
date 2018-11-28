import sys


def solve(state: str, n):
    n = int(n)
    result = 0
    while True:
        print('!', state)
        state = state.lstrip('+')
        print('.', state)
        if not state:
            return result
        if len(state) < n:
            return 'IMPOSSIBLE'
        if '+' not in state:
            return result + int(len(state) / n) if len(state) % n == 0 else 'IMPOSSIBLE'
        k = state.find('+')
        print('k =', k)
        if k >= n:
            result += int(k / n)
            state = state[k - (k % n):]
        else:
            result += 1
            print('p', state[k:n], ''.join('+' if c == '-' else '-' for c in state[k:n]))
            state = ''.join('+' if c == '-' else '-' for c in state[k:n]) + state[n:]
        print('?', state)


with open(r'D:\Downloads\A-large.in') as f, open(r'D:\Downloads\A-l.out', 'w') as out_f:
    print('\n'.join(['Case #{}: {}'.format(i + 1, solve(*line.strip().split(' ', 1))) for i, line in enumerate(f.readlines()[1:])]), file=out_f)
import sys
import collections

def solve(S, K):
    deq = collections.deque([(S, 0)])
    perms = set()
    while len(deq) > 0:
        S, depth = deq.popleft()
        if is_solved(S):
            return depth
        if S not in perms:
            deq.extend((flip(S, i, K), depth + 1) for i in range(len(S) - K + 1))
            perms.add(S)
    return None

def is_solved(S):
    return '-' not in S

def flip(S, i, K):
    chars = [ch for ch in S]
    for idx in range(i, i + K):
        chars[idx] = '+' if chars[idx] == '-' else '-'
    return ''.join(chars)

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        T = int(f.readline().strip())
        for case in range(T):
            S, K = f.readline().strip().split()
            sol = solve(S, int(K))
            if sol is None:
                print('Case #{}: IMPOSSIBLE'.format(case + 1))
            else:
                print('Case #{}: {}'.format(case + 1, sol))

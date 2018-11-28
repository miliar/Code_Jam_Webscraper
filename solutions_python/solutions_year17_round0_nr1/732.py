import sys

def solve(states, k):
    states = [1 if s == '-' else 0 for s in states.strip()]
    ends = [0]*(len(states)+1)
    nflips = 0
    currentflips = 0
    for i, v in enumerate(states):
        currentflips += ends[i]
        if i > len(states)-k:
            if (currentflips%2) != states[i]:
                return 'IMPOSSIBLE'
        else:
            if (currentflips%2) != states[i]:
                currentflips += 1
                nflips += 1
                ends[i+k] = -1
    return nflips

if __name__ == '__main__':
    lines = sys.stdin.readlines()[1:]
    for t, l in enumerate(lines):
        states, k = l.split()
        k = int(k)
        print('Case #{}: {}'.format(t+1, solve(states, k)))

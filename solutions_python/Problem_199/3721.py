def main():
    n = int(raw_input())
    for i in range(n):
        line = raw_input().split(' ')
        states = list(line[0])
        k = int(line[1])
        solution = solve(states, k)
        msg = solution if solution > -1 else 'IMPOSSIBLE'
        print('Case #{}: {}'.format(i + 1, msg))

def toggle(ch):
    return '-' if ch == '+' else '+'

def solve(states, k):
    def flip_k(start):
        for i in range(start, start + k):
            states[i] = toggle(states[i])

    flips = 0
    last_flip = len(states) - k + 1

    for i in range(last_flip):
        if (states[i] == '-'):
            flip_k(i)
            flips += 1

    for ch in states[last_flip:]:
        if ch == '-':
            return -1
    
    return flips

if __name__ == '__main__':
    main()

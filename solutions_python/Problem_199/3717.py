
import sys

def __flip(m):
    def reverse(c):
        if c == '-':
            return '+'
        else:
            return '-'
    return ''.join([reverse(c) for c in m])

def flip(s, idx, k):
    h, m, t = s[:idx], s[idx:idx+k], s[idx+k:]
#    print('\t{}, {}, {}'.format(h, m, t))
    return h + __flip(m) + t

def solv(s, k):
    flip_count = 0
    for i in range(0, len(s)-k+1):
#        print(s)
        if s[i] == '-':
            s = flip(s, i, k)
            flip_count += 1
    if '-' in s:
        return 'IMPOSSIBLE'
    return str(flip_count)

def main(filename):
    with open(filename, 'r') as f:
        t = int(f.readline())
        for ti in range(1, t+1):
            s, k = f.readline().split()
            r = solv(s, int(k))
            print('Case #{}: {}'.format(ti, r))

if __name__ == '__main__':
    main(sys.argv[1])

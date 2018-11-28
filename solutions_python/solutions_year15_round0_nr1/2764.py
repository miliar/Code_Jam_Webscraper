import sys

def solve(s_max, aud):
    invites = 0
    standing = 0
    # first case: no s_i = 0
    for i, a in enumerate(aud):
        if i == 0 and a == 0:
            invites += 1
            standing += 1
            continue
        while standing < i:
            invites += 1
            standing += 1
        standing += a
    return invites


def main():
    with open(sys.argv[1]) as f:
        T = int(f.readline())
        for i in xrange(T):
            s_max, aud = f.readline().strip().split()
            s_max = int(s_max)
            aud = map(int, list(aud))
            print 'Case #{}: {}'.format(i+1, solve(s_max, aud))
if __name__ == '__main__':
    main() 
import sys


def main():
    t = int(sys.stdin.readline())
    for k in range(t):
        s_max, s = sys.stdin.readline().strip().split()
        s_max = int(s_max)
        s = list(map(int, s))

        standing = 0
        total_invited = 0
        for i, si in enumerate(s):
            if standing < i:
                invited = i - standing
                standing += invited
                total_invited += invited
            standing += si

        print ('Case #%d: %d' % (k + 1, total_invited))

if __name__ == '__main__':
    main()

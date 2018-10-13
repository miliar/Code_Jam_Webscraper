#!/usr/bin/python


def output(num, msg):
    print 'Case #%d: %s' % (num, msg)

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        flips = 0
        pancakes, K = raw_input().split(' ')
        K = int(K)
        pancakes = map(lambda x: 0 if x == '-' else 1, pancakes)
        for i in range(len(pancakes) - K + 1):
            if pancakes[i] == 0:
                for k in range(i, i + K):
                    pancakes[k] = 1 - pancakes[k]
                flips += 1
        if all(p == 1 for p in pancakes):
            output(t, flips)
        else:
            output(t, 'IMPOSSIBLE')


if __name__ == '__main__':
    main()

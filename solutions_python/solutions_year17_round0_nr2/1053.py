#!/usr/bin/env python
# pylint:disable=missing-docstring,invalid-name


def main():
    rs = int(raw_input())
    for rn in range(rs):
        print 'Case #%d: ' % (rn + 1),

        n = [int(x) for x in raw_input()]

        feq = 0
        for i, x in enumerate(n):
            if x == n[feq]:
                pass
            elif x > n[feq]:
                feq = i
            else:
                n[feq] -= 1
                for j in range(feq + 1, len(n)):
                    n[j] = 9
                break

        if n[0] == 0 and len(n) > 1:
            n = n[1:]
        print ''.join(str(x) for x in n)


if __name__ == '__main__':
    main()

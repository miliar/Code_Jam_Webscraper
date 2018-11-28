#!/usr/bin/env python3
import sys

DATA = '''3
---+-++- 3
+++++ 4
-+-+- 4
'''

def flip(x):
    n, k = x.replace('-','0').replace('+','1').strip().split()
    m = len(n)
    n = int(n, 2)
    k = int(k)

    q = 2**k - 1
    n ^= 2**m - 1
    flips = 0
    for i in range(m - k + 1):
        if n % 2 == 1:
            flips += 1
            n ^= q
        n >>= 1
    if n == 0:
        return flips
    else:
        return 'IMPOSSIBLE'

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        from io import StringIO
        fh = StringIO(DATA)
        oh = sys.stdout
    else:
        fh = open(sys.argv[1], 'r')
        oh = open('output.txt', 'w')
    with fh:
        with oh:
            for i, line in enumerate(fh.readlines()):
                if i == 0:
                    continue
                print('Case #{}: {}'.format(i, flip(line)), file=oh)


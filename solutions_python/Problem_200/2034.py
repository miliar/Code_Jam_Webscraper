#!/usr/bin/env python3
def tidy(x):
    s = list(str(x))
    n = len(s)
    for i in range(n - 1):
        if s[i] > s[i+1]:
            return tidy(int(''.join(s[:i+1]) + '0'*(n - i - 1)) - 1)
    else:
        return x

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as fh:
        with open('output.txt','w') as oh:
            for i, line in enumerate(fh.readlines()):
                if i == 0:
                    continue
                print('Case #{}: {}'.format(i, tidy(int(line))), file=oh)


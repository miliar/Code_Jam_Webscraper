#! /usr/bin/env python
# -*- coding: utf-8 -*

def is_good(s):
    for i in xrange(1, len(s)):
        if s[i-1] <= s[i]:
            pass
        else:
            return False
    return True


def solve(snum):
    N = len(snum)
    if N == 1 or is_good(snum):
        return int(snum)
    num = int(snum)
    out = 0
    for i in xrange(len(snum)):
        if snum[i] > 0:
            cur = snum[:i:] + str(int(snum[i]) - 1) + '9' * (N - i - 1)
            if is_good(cur) and num - out >= num - int(cur):
                out = int(cur)
    return out


def main():
    n = int(raw_input().strip())
    for test in xrange(1, n + 1):
        snum = raw_input().strip()
        print 'Case #%d: %d' % (test, solve(snum))

if __name__ == "__main__":
  main()

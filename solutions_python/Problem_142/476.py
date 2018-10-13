#! /usr/bin/python
import itertools

def solve(strs):
    parts = map(spl, strs)
    if any(len(p) != len(parts[0])
           or any(c1 != c2 for (c1, sz1), (c2, sz2) in zip(p, parts[0]))
                  for p in parts[1:]):
        return 'Fegla Won'
    return sum(abs(pcs[0][1] - pcs[1][1])
               for pcs in zip(*parts))

def spl(s):
    return list((c, len(list(group)))
                for c, group in itertools.groupby(s, lambda c: c))

def main():
    t = input()
    for i in xrange(1, t + 1):
        n = input()
        strs = list(raw_input() for j in xrange(n))
        print 'Case #{0}: {1}'.format(i, solve(strs))


if __name__ == '__main__':
    main()

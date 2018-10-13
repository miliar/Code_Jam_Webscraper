#!/usr/bin/env python

import sys

def get_counts(s):
    if not s:
        return []
    counts = [1]
    chars = [s[0]]
    for i in xrange(1, len(s)):
        if s[i] == chars[-1]:
            counts[-1] += 1
        else:
            counts.append(1)
            chars.append(s[i])
    return counts, chars

def get_min(strings):
    all_counts, all_chars = [], []
    for s in strings:
        counts, chars = get_counts(s)
        all_counts.append(counts)
        all_chars.append(tuple(chars))
    if len(set(all_chars)) != 1:
        return None
    mins = []
    for i in xrange(len(all_counts[0])):
        values = [c[i] for c in all_counts]
        mu = sum(values) / len(values)
        m1 = sum(abs(_ - mu) for _ in values)
        mu += 1
        m2 = sum(abs(_ - mu) for _ in values)
        mins.append(min(m1, m2))
    return sum(mins)

def main(in_stream, out_stream):
    n_cases = int(in_stream.next())
    for i in xrange(1, n_cases+1):
        N = int(in_stream.next())
        strings = [in_stream.next().rstrip() for _ in xrange(N)]        
        m = get_min(strings)
        res = "%d" % m if m is not None else 'Fegla Won'
        out_stream.write('Case #%d: %s\n' % (i, res))

if __name__ == '__main__':
    main(sys.stdin, sys.stdout)

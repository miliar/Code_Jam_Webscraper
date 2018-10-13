#!/usr/bin/env python

import sys

f = sys.stdin

T = int(f.readline())

for t in xrange(1, T+1):
    case = f.readline().split()
    C = int(case.pop(0))
    repl = {}
    for c in xrange(C):
        word = case.pop(0)
        a, b, c = word
        repl[a+b] = c
        repl[b+a] = c
    D = int(case.pop(0))
    vanish = {}
    for d in xrange(D):
        word = case.pop(0)
        a, b = word
        if a not in vanish:
            vanish[a] = set()
        vanish[a].add(b)
        if b not in vanish:
            vanish[b] = set()
        vanish[b].add(a)

    word_len = int(case.pop(0))

    word = case.pop(0)
    new_word = []
    char_counts = dict([(chr(x + ord('A')), 0) for x in range(26)])
    for c in word:
        new_word.append(c)
        char_counts[c] += 1
        while len(new_word) >= 2:
            last2 = new_word[-2] + new_word[-1]
            if last2 in repl:
                char_counts[new_word[-2]] -= 1
                char_counts[new_word[-1]] -= 1
                char_counts[repl[last2]] += 1
                new_word.pop()
                new_word.pop()
                new_word.append(repl[last2])
            else:
                killed = False
                for c, count in char_counts.iteritems():
                    if count > 0:
                        for killer in vanish.get(c, []):
                            if char_counts[killer] > 0:
                                new_word = []
                                char_counts = dict([(chr(x + ord('A')), 0) for x in range(26)])
                                killed = True
                                break
                    if killed:
                        break
                break

    print "Case #%d: [%s]" % (t, ', '.join(new_word))

#!/usr/bin/python3

from sys import argv
import re

def points(word, words, order):
    # print('Word: ' + word)
    # print('Order: ' + order)
    known = bytearray('.' * len(word), 'ASCII')
    goodwords = words[:]
    p = 0
    picklet = 0
    while known.decode('ASCII') != word:
        i = 0
        letters = []
        knownstr = '^' + known.decode('ASCII') + '$'
        while i < len(goodwords):
            if re.match(knownstr, goodwords[i]):
                for l in goodwords[i]:
                    if l not in letters:
                        letters.append(l)
                i += 1
            else:
                del goodwords[i]
        # print(' '.join(goodwords))
        for i in range(picklet, len(order)):
            if order[i] in letters:
                # print('Pick {}'.format(order[i]))
                picklet = i+1
                if order[i] in word:
                    countlet = 0
                    for j, l in enumerate(word):
                        if order[i] == l:
                            known[j] = ord(order[i])
                            countlet += 1
                    # I need to throw out words that have the letter in other positions!
                    j = 0
                    while j < len(goodwords):
                        countlet2 = 0
                        for k in goodwords[j]:
                            if k == order[i]:
                                countlet2 += 1
                        if countlet2 != countlet:
                            del goodwords[j]
                        else:
                            j += 1
                else:
                    p += 1
                    j = 0
                    while j < len(goodwords):
                        if order[i] in goodwords[j]:
                            del goodwords[j]
                        else:
                            j += 1
                # print('Known ' + known.decode('ASCII'))
                break
    # print('{} points'.format(p))
    # print()
    return p

infile = open(argv[1])
t = int(infile.readline())
for i in range(t):
    n, m = map(int, infile.readline().split())
    word = []
    order = []
    for j in range(n):
        word.append(infile.readline().rstrip('\n'))
    for j in range(m):
        order.append(infile.readline().rstrip('\n'))
    maxwords = []
    for o in order:
        maxpoints = -1
        for w in word:
            p = points(w, word, o)
            if p > maxpoints:
                maxpoints = p
                maxword = w
        maxwords.append(maxword)
    print('Case #{}: {}'.format(i+1, ' '.join(maxwords)))

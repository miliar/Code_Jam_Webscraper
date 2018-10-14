#!/usr/bin/python
import sys
from sys import stderr

def pos(c):
    return ord(c) - ord('a')

def Sean(word, ldi, letters):
    words = ldi[0][:]
    freq = ldi[1][:]
    points = 0
    #print >>stderr, word, words, freq, letters
    for c in letters:
        if len(words) == 1:
            break
        f = freq[pos(c)]
        if f == 0:
            continue
        #print >>stderr, "Try", c

        remove = set()
        count = word.count(c)
        if count > 0:  # hit
            for rem in words:
                if rem.count(c) != count:
                    remove.add(rem)
                else:
                    for i,w in enumerate(word):
                        if w == c and rem[i] != c:
                            remove.add(rem)
        else:
            points += 1 # fail
            for rem in words:
                if c in rem:
                    remove.add(rem)

        for rem in remove:
            words.remove(rem)
            for c in rem:
                freq[pos(c)] -= 1
        #print >>stderr, points, words, freq
    return points
    

def Solve(di, li):
   #print >>stderr, "*********"
   #print >>stderr, di, "\n", li

    ldi = [None, 
            ([], [0] * 26), 
            ([], [0] * 26), 
            ([], [0] * 26), 
            ([], [0] * 26), 
            ([], [0] * 26), 
            ([], [0] * 26), 
            ([], [0] * 26), 
            ([], [0] * 26), 
            ([], [0] * 26), 
            ([], [0] * 26)
            ]

    for word in di:
        for c in word:
            ldi[len(word)][1][pos(c)] += 1
        ldi[len(word)][0].append(word)


    reply = []
    for letters in li:
        nmax = -1
        wmax = None
        for word in di:
            n = Sean(word, ldi[len(word)], letters) 
           #print >>stderr, "Sean", word, n
            if n > nmax:
                nmax = n
                wmax = word
        reply.append(wmax)
       #print >>stderr, nmax, wmax

    return " ".join(reply)


f = open(sys.argv[1])

T = int(f.readline())
for t in range(T):
    ndict, nlist = map(int, f.readline().split())
    di = []
    li = []
    for i in range(ndict):
        di.append(f.readline().strip())
    for i in range(nlist):
        li.append(f.readline().strip())
    print "Case #%d: %s" % (t+1, Solve(di, li))




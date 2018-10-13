import os, sys

infile = open(sys.argv[1], "r")
T = int(infile.readline())
lex = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}
for x in xrange(T):
    words = infile.readline().split()
    solved = ""
    for word in words:
        for y in xrange(len(word)):
            if word[y] in lex:
                solved += lex[word[y]]
            else:
                solved += "_"
        solved += " "
    print "Case #%d: %s" % (x+1, solved.rstrip())
# Mallin Moolman

import re

filename = "A-large.in"
f = open (filename)
outfile = open (filename.rsplit(".", 1)[0] + ".out", 'w')
l, d, n = [int(x) for x in f.readline().strip().split(" ")]

words = []
for i in xrange (d):
    # read words
    line = f.readline()
    words.append (line.strip())



for j in xrange (n):
    #each error-prone word
    wordsc = words[:]
    tokens = [ss.strip("()") for ss in re.findall ("\([a-z]*\)|[a-z]", f.readline().strip())]

    matched = 0
    for word in wordsc:
        matches = True
        for index in xrange(len(word)):
            if not word[index] in tokens[index]:
                matches = False
        if matches:
            matched += 1

    outfile.write( "Case #%d: %d\n" % (j+1, matched))
    




f.close()
outfile.close()

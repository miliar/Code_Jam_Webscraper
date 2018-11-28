import sys
import re

def cnt_loop(words, vocabSet, words_partial, acum="", cnt=0):
    for l in words[0]:
        curr_wrd = acum + l
        if len(words)==1:
            if curr_wrd in vocabSet:
                cnt += 1
        else:
            if curr_wrd in words_partial:
                cnt = cnt_loop(words[1:], vocabSet, words_partial, curr_wrd, cnt)
    return cnt



lines = [x.strip() for x in open(sys.argv[1]).readlines()]

# Extract config
L, D, N = [int(x) for x in lines[0].split(" ")]

# Read words in language
words = set()
words_partial = set()
for i in xrange(1, D+1):
    words.add( lines[i] )
    for j in xrange(len(lines[i])):
        words_partial.add( lines[i][:j+1] )

for line_nbr, line in enumerate(lines[D+1:D+1+N]):
    comb_acum = []
    for m in re.finditer(r"(?i)(?:\([a-z]+\)|[a-z])", line):
        if len(m.group(0))==1:
            comb_acum.append( m.group(0) )
        else:
            comb_acum.append( m.group(0)[1:-1] )

    print "Case #%d: %d" % (line_nbr+1, cnt_loop(comb_acum, words, words_partial))

import string
import math

testcase = open('testcase', 'r')
num_cases = int(string.strip(testcase.readline()))


def do_calc(i):
    n = int(string.strip(testcase.readline()))
    strings = []
    for j in xrange(n):
        strings.append(string.strip(testcase.readline()))
    canonicalization = []
    copies = []
    curr_char = strings[0][0]
    canonicalization.append(curr_char)
    curr_copies = 1
    this_copies = []
    for char in strings[0][1:]:
        if char != curr_char:
            curr_char = char
            canonicalization.append(char)
            this_copies.append(curr_copies)
            curr_copies = 1
        else:
            curr_copies += 1
    this_copies.append(curr_copies)
    copies.append(this_copies)
    for s in strings[1:]:
        curr_char = s[0]
        idx = 0
        curr_copies = 1
        this_copies = []
        if canonicalization[idx] != curr_char:
            print "Case #"+str(i)+": Fegla Won"
            return
        for char in s[1:]:
            if char != curr_char:
                curr_char = char
                idx += 1
                if idx >= len(canonicalization) or canonicalization[idx] != curr_char:
                    print "Case #"+str(i)+": Fegla Won"
                    return
                this_copies.append(curr_copies)
                curr_copies = 1
            else:
                curr_copies += 1
        if s[-1] != canonicalization[-1]:
            print "Case #"+str(i)+": Fegla Won"
            return
        this_copies.append(curr_copies)
        copies.append(this_copies)
#    print copies
#    print len(copies[0]), len(copies[1])
#    print len(canonicalization)
#    print canonicalization
#    print n
    moves = 0
    for k in xrange(len(canonicalization)):
        vals = [copies[x][k] for x in xrange(n)]
        moves += (max(vals) - min(vals))
    print "Case #"+str(i)+": "+str(moves)

for i in xrange(1, num_cases+1):
    do_calc(i)

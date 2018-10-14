#!python

class NTree:
    children = {}
    val = ""
    def __init__(self, v):
        self.children = {}
        self.val = v
    def add_child(self, n_v):
        next_tree = NTree(n_v)
        return self.children.setdefault(n_v, next_tree)

    def print_string(self, curr_level):
#        print "CURRENT LEVEL: %d" % (curr_level)
        for i in xrange(0, curr_level):
            print "\t",
        print "%s" % (self.val)
        for c in self.children.keys():
            for i in xrange(0, curr_level + 1):
                print "\t",
            self.children[c].print_string(curr_level + 1)

    def num_matches(self, match_string):
        if match_string == "":
            return 1

        if match_string[0] != "(":
            if self.children.setdefault(match_string[0], 0):
                return self.children[match_string[0]].num_matches(
                    match_string[1:])
            else:
                return 0

        poss = ""
        i = 1
        while match_string[i] != ")":
            poss += match_string[i]
            i += 1
        match_string = match_string[i+1:]
        total_matches = 0
        for p in poss:
            total_matches += self.num_matches(p + match_string)
        return total_matches

import sys

if len(sys.argv) != 2:
    print "Must take only a filename as an argument."
    exit(-1)

filename = sys.argv[1]
fh = open(filename, 'r')
fn = fh.read().split('\n')

format = fn[0]

fields = format.split()

l = int(fields[0])
d = int(fields[1])
n = int(fields[2])

word_list = fn[1:1+d]
test_cases = fn[1+d:]

words = NTree("")
for i in xrange(0, d):
    word = word_list[i]
    curr_tree = words
    for j in xrange(0, l):
        letter = word[j]
        curr_tree = curr_tree.add_child(letter)

for i in xrange(0, n):
#    sys.stderr.write("Solving case %d" % (i))
    print "Case #%d: %d" % (i+1, words.num_matches(test_cases[i]))
    

fh.close()

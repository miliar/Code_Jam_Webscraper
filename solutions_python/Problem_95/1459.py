#!/usr/bin/env python
#from collections import defaultdict

google = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
          "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
          "de kr kd eoya kw aej tysr re ujdr lkgc jv",
          "y qee"]
 
english = ["our language is impossible to understand",
           "there are twenty six factorial possibilities",
           "so it is okay if you want to just give up",
           "a zoo"]
def make_stone(l1, l2):
    stone = {'z':'q'}
    for i,line in enumerate(l1):
        for j, character in enumerate(line):
            if character in stone and stone[character] != l2[i][j]:
                print i, j, 'error'
            stone[character] = l2[i][j]
    return stone
stone = make_stone(google, english)

def use_stone(old_line, stone):
    new_line = ""
    for c in old_line:
        new_line += stone[c]
    return new_line

def processFile(fname):
    def processCase(f):
        googlerese = f.readline().strip("\n")
        return use_stone(googlerese, stone)
    
    with open(fname, "r") as f:
        cases = int(f.readline().strip("\n"))
        output = ""
        for case in range(cases):
            a = processCase(f)
            output += "Case #%d: %s\n" % (case + 1, a)
        print output
    with open("ans"+fname, "w") as f:
        f.write(output)

#processFile("sample.txt")
processFile("A-small-attempt0.in")
#processFile("B-large.in")
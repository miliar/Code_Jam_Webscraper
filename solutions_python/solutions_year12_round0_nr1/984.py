"""
We have come up with the best possible language here at Google, called Googlerese. 
To translate text into Googlerese, we take any message and replace each English letter 
with another English letter. This mapping is one-to-one and onto, which means that the 
same input letter always gets replaced with the same output letter, and different input 
letters always get replaced with different output letters. A letter may be replaced by 
itself. Spaces are left as-is.

For example (and here is a hint!), our awesome translation algorithm includes the following 
three mappings: 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'. 
This means that "a zoo" will become "y qee".

Googlerese is based on the best possible replacement mapping, and we will never change it. 
It will always be the same. In every test case. We will not tell you the rest of our mapping 
because that would make the problem too easy, but there are a few examples below that may help.

Given some text in Googlerese, can you translate it to back to normal text?
Solving this problem

Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has 
only 1 Small input. Once you have solved the Small input, you have finished solving this problem.
Input

The first line of the input gives the number of test cases, T. T test cases follow, one per line.

Each line consists of a string G in Googlerese, made up of one or more words containing the 
letters 'a' - 'z'. There will be exactly one space (' ') character between consecutive words 
and no spaces at the beginning or at the end of any line.


Output

For each test case, output one line containing "Case #X: S" where X is the case number and S is 
the string that becomes G in Googlerese.
Limits

1 <= T <= 30.
G contains at most 100 characters.
None of the text is guaranteed to be valid English.
Sample

Input
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv

Output
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up
"""

import util
import sys

rosetta = {}
rosetta[0] = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"]
rosetta[1] = ["rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"]
rosetta[2] = ["de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"]
rosetta[3] = ["y qee", "a zoo"]
rosetta[4] = ["z", "q"]


def makeDict(rosetta):
    translation = {}
    for j in rosetta:
        clue = rosetta[j]
        for i in range(len(clue[1])):
            k = clue[0][i]
            v = clue[1][i]
            if k in translation.keys():
                if translation[k] != v:
                    raise Exception("Key:%s Value:%s exists but the stored value is:%s " % (k, v, translation[k]))
            translation[k] = v
    return translation

def translate():
    translation = makeDict(rosetta)
    util.debug("translation dict: ")        
    util.debug(translation)
    
    values = [translation[k] for k in translation]
    util.debug("")
    util.debug("value dict: ")        
    util.debug(sorted(values))
    return translation

def decrypt(translation, f):
    in_file = f
    words = util.readFile(in_file, True, 1)[1:]    
    test_n = 1
    
    with open(in_file + "_out", "w") as f:
        for w in words:
            out = ""
            for c in w:
                out += translation[c]
            util.debug("input:%s " % w)
            out = "Case #%s: %s" % (test_n, out)
            f.write(out + "\n")
            test_n += 1
            util.debug("out:%s " % out)


def main():
    translation = translate()
    decrypt(translation, sys.argv[1])
    

if __name__ == "__main__":
    main()



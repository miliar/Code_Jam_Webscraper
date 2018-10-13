#/usr/bin/python

import sys

def matches(word, pattern):
    for i in xrange(len(word)):
        if word[i] not in pattern[i]:
            return False
    return True

def parsePattern(pattern, length):
    tokens = []
    i = 0
    while len(tokens) < length:
        if pattern[i] == '(':
            l = []
            i += 1
            while pattern[i] != ')':
                l.append(pattern[i])
                i += 1
            tokens.append(l)
        else:
            tokens.append([pattern[i]])
        i += 1
    return tokens

def main():
    inputFile = sys.argv[1]
    f = open(inputFile, 'r')
    length, noOfWords, testCases  = [int(n) for n in f.readline().split()]
    words = [f.readline().strip() for i in xrange(noOfWords)]
    patterns = [parsePattern(f.readline().strip(), length) for i in xrange(testCases)]
    for i in xrange(len(patterns)):
        count = 0
        for word in words:
            if matches(word, patterns[i]):
                count += 1
        print "Case #" + str(i + 1) + ": " + str(count)

main()

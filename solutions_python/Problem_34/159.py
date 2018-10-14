#!/usr/bin/python

import sys

LEFT_PAREN = '('
RIGHT_PAREN = ')'

def parse(test):

    data = []
    s = str(test)

    while s:
        c = s[0]

        if c == LEFT_PAREN:
            pre, it, s = s.partition(RIGHT_PAREN)
            if pre:
                data.append(pre[1:])

        else:
            data.append(c)
            s = s[1:]

    return data


def reduce(words, options, i, part):

    updated = []

    for option in options:

        word = words[option]
        c = word[i]
        
        if c in part:
            updated.append(option)

    return updated



def main():

    if len(sys.argv) < 2:
        print "need file"
        return

    L, D, N = 0, 0, 0

    words = None
    tests = None

    with open(sys.argv[1]) as file:

        l, d, n = file.readline().split()
        L, D, N = int(l), int(d), int(n)

        words = [file.readline().rstrip() for i in xrange(D)]
        tests = [file.readline().rstrip() for i in xrange(N)]

    #print words
    #print tests

    for n, test in enumerate(tests):
        data = parse(test)

        options = range(len(words))

        for i, part in enumerate(data):
            options = reduce(words, options, i, part)

        #print options
        print "Case #{0}: {1}".format(n + 1, len(options))


if __name__ == "__main__":
    main()


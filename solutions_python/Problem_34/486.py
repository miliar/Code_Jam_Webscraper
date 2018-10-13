#! /usr/bin/env python

import sys
import re



def count_possible(pattern, dict):
    """Return the number of matches for pattern with words in dict.
    All words in dict must be of length wlen.
    pattern is a compiled RegexObject.
    """
    count = 0
    for word in dict:
        if pattern.match(word):
            count += 1

    return count


def main(argv):
    input = sys.stdin
    
    firstline = input.readline()
    L, D, N = [int(i) for i in firstline.split()]

    alien_dict = []   # all the words in the language
    for i in xrange(D):
        alien_dict.append(input.readline())

    if not all(len(word) == (L + 1) for word in alien_dict):
        raise Exception('Invalid dictionary!')

    for i in xrange(N):
        pattern = input.readline()
        re_pattern = re.compile(pattern.replace('(', '[').replace(')', ']'))
        possible = count_possible(re_pattern, alien_dict)
        print 'Case #%d: %d' % ((i + 1), possible)
    

if __name__ == '__main__':
    sys.exit(main(sys.argv))

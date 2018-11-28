#!/usr/bin/python

import sys
import bisect
import itertools

pdrome_max = 10**14

def is_pdrome(num):
    s = str(num)
    sLen = len(s)
    for a, b in zip(s[:(sLen+1)//2], reversed(s[(sLen+1)//2:])):
        if a != b:
            return False
    return True

def get_pdromes(pdrome_max):
    pdromes = []
    for i in itertools.count(1):
        i2 = i**2;
        if i2 > pdrome_max:
            break
        if is_pdrome(i) and is_pdrome(i2):
            pdromes.append(i2)
    return pdromes

pdromes = get_pdromes(pdrome_max)

def main():
    sys.stdin.readline()
    for tc_num, line in enumerate(sys.stdin.readlines()):
        A, B = (int(i) for i in line.split())
        num_pdromes = bisect.bisect(pdromes, B) - bisect.bisect_left(pdromes, A)
        print "Case #%d: %d" % (tc_num + 1, num_pdromes)

if __name__ == "__main__":
    main()

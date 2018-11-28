import sys

trans ={' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q'}

def main(ifile, ofile):
    n = int(ifile.readline())
    for i in range(n):
        line = ifile.readline().strip()
        res = ''
        for x in line:
            res += trans[x]
        ofile.write("Case #%s: " % (i+1) + res + '\n')

import sys
main(sys.stdin, sys.stdout)


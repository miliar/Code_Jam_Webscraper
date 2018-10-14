#!/usr/bin/python

import os
import sys

if __name__ == "__main__":

    mapping = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ': ' ', 'q':'z'}
    input_file = open(sys.argv[1])
    T = int(input_file.readline().strip())
    for i in range(T):
        out = "Case #%d: " % (i+1)
        line = input_file.readline().strip()
        for letter in line:
            out += mapping[letter]
        print out

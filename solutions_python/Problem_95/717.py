'''
Created on Apr 13, 2012

@author: scyrmion
'''
import sys

#copied from output of learn.py
mappings={'\n': '\n', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def convert(text):
    return ''.join(mappings[char] for char in text)

def writeOutput(caseNum, output, outfile):
    outfile.write("Case #{0}: {1}".format(caseNum, output))

if __name__ == '__main__':
    infile = open("A-small-attempt0.in")
    outfile = open("output.txt", 'w')
    lines = infile.readlines()
    if int(lines[0])!=len(lines)-1:
        print("Invalid number of inputs.\n", file=sys.stderr)
        exit(1)
    for i, line in enumerate(lines[1:]):
        writeOutput(i+1, convert(line), outfile)
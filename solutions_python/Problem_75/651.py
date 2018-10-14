#!/usr/bin/python

from optparse import OptionParser
import operator

def parseOptions():
    parser = OptionParser()
    parser.add_option('-i', '--input', dest = 'input', help = 'Input file', default = 'C-small-practice.in')
    # parser.add_option('-o', '--output', dest = 'output', help = 'Output file', default = 'output.txt')
    (options, args) = parser.parse_args()
    return options

def readParameters(options):
    input = open(options.input)
    n = int(input.readline().strip())
    combines, opposed, numChars, strings = [], [], [], []
    for i in xrange(n):
        vals = input.readline().strip().split()
        numCombines = int(vals[0])
        tempCombine = {}
        for j in xrange(numCombines):
            baseElements = tuple(sorted(vals[1+j][:2]))
            target = vals[1+j][-1]
            tempCombine[baseElements] = target
        combines.append(tempCombine)
        numOpposed = int(vals[1+numCombines])
        tempOpposed = set([])
        for j in xrange(numOpposed):
            tempOpposed.add(tuple(sorted(vals[2+numCombines])))
        opposed.append(tempOpposed)
        numChars.append(int(vals[2+numCombines+numOpposed]))
        strings.append(vals[-1])
    return n, combines, opposed, numChars, strings

def applyTransforms(combines, opposed, numChars, s):
    s = list(s)
    i = 1
    while i < numChars and i < len(s):
        current2Chars = tuple(sorted(s[i-1:i+1]))
        if current2Chars in combines:
            s[i-1:i+1] = combines[current2Chars]
            i -= 1
        else:
            for j in xrange(i):
                current2Chars = tuple(sorted([s[j], s[i]]))
                if current2Chars in opposed:
                    s[:i+1] = []
                    i = 0
                    break
        i += 1
    return '[' + ', '.join(s) + ']'

def main(options):
    n, combines, opposed, numChars, strings = readParameters(options)
    results = []
    for i in xrange(n):
        result = applyTransforms(combines[i], opposed[i], numChars[i], strings[i])
        results.append('Case #%d: %s' % (i+1, result))
    open(options.input.replace('.in', '.out'), 'w').write('\n'.join(results))
    for r in results:
        print r

if __name__ == "__main__":
    options = parseOptions()
    main(options)

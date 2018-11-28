#-------------------------------------------------------------------------------
# Name:         cjinput
# Purpose:      CodeJam Input Processor
#
# Author:       Ben Jolly
#
# Created:      26/04/2011
# Copyright:    (c) Ben Jolly 2011
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import re

def defaultCaseIterator(filehandle):
    numcases = int(filehandle.readline())
    cases = []
    for line in filehandle:
        cases.append(line.strip())

    filehandle.close()

    return cases

def defaultStrConverter(arg):
    if arg is type(''):
        return arg
    else:
        return str(arg)

def int1DArrayConverter(arg):
    return list(int(element) for element in re.split('[ \t,]+', arg))

class cjinput:

    global fn, outfn, cases, outputfile, outputcount

    def __init__(self, fn, outputfn, caseiterator=defaultCaseIterator):
        self.fn = fn
        self.outfn = outputfn
        self.cases = caseiterator(open(fn))

    def testcases(self, converter=defaultStrConverter):
        self.outputfile = open(self.outfn, 'w')
        self.outputcount = 1

        for case in self.cases:
            yield converter(case)

        self.outputfile.close()

    def writeoutput(self, result, specific_case=None, debug=True):
        if debug:
            print('Case #%d: %s' %(self.outputcount, defaultStrConverter(result)))

        self.outputfile.write('Case #%d: %s\n' %(self.outputcount, defaultStrConverter(result)))
        self.outputcount += 1

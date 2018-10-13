#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Google Cod Jam
Lawnmower
https://code.google.com/codejam/contest/2270488/dashboard#s=p1
"""

import sys
import os
import traceback
import argparse
import time
import re
from CodeJam import CodeJam

#from pexpect import run, spawn

def debug(*vals, **kwargs):
    global args
    if args.verbose:
        print(*vals, **kwargs)

class Mower(CodeJam):

    def addGrid(self, elements):
        self.pattern=elements
        self.swapped=list(zip(*elements))

    def getResults(self):
        return "YES" if self.checkRows() else "NO"

    def checkRows(self):
        for rowIdx, row in enumerate(self.pattern):
            maxH = max(row)
            shorterIndexes = [idx for idx,val in enumerate(row) if val < maxH]
            for colIdx in shorterIndexes:
                cellValue = self.pattern[rowIdx][colIdx]
                if not self.checkCol(colIdx, cellValue):
                    return False
        return True

    def checkCol(self, colIdx, cellValue):
        # using swapped
        col = self.swapped[colIdx]
        maxCol = max(col)
        return maxCol == cellValue


    def run(self):
        pattern = []
        patternCount = 0
        section = 0 # 0=NM 1 = elements
        rows = 0
        for lineNum, line in self.getInput():
            if lineNum== 0:
                total = int(line)
                continue
            if section == 0:
                rows = int(line.split(' ')[0]) # first num is rows
                debug('In 0:')
                debug("Number of rows: %d" % (rows))
                section = 1
            elif section == 1:
                vals=[int(x) for x in line.split(' ')]
                debug("In 1:")
                debug(vals)
                pattern.append(vals)
                if len(pattern) == rows:
                    debug("Pattern to check:")
                    debug(pattern)
                    self.addGrid(pattern)
                    patternCount += 1
                    result = self.getResults()
                    self.writeOutput(patternCount,result)
                    section = 0
                    pattern = []
                    

        if patternCount != total:
            print("ERROR: Expected %d, got %d boards" % (total,patternCount))



def main():

    global args
    # TODO: Do something more interesting here...
    m=Mower(args.inFile)

    m.addGrid([
        [2,1,2],
        [1,1,1],
        [2,1,2]
        ])
    debug(m.getResults())
    m.addGrid([
        [1,2,1]
        ])
    debug(m.getResults())
    m.addGrid([
        [2,2,2,2,2],
        [2,1,1,1,2],
        [2,1,2,1,2],
        [2,1,1,1,2],
        [2,2,2,2,2]
        ])
    debug(m.getResults())
    m.run()


if __name__ == '__main__':
    try:
        start_time = time.time()
        # Parser: See http://docs.python.org/dev/library/argparse.html
        parser = argparse.ArgumentParser(description='Python script')
        parser.add_argument('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_argument('-ver', '--version', action='version', version='1.0')
        parser.add_argument('inFile')
        args = parser.parse_args()
        debug(time.asctime())
        main()
        debug(time.asctime())
        debug("Total time in seconds: ", end="")
        debug((time.time() - start_time))
        sys.exit(0)
    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
    except SystemExit as e:  # sys.exit()
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        traceback.print_exc()
        os._exit(1)


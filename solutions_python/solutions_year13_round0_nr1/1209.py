#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Google CodeJam Helper
[Name]
[URL]
"""

import sys
import os
import traceback
import argparse
import time
import re
#from pexpect import run, spawn



class CodeJam:


    def __init__(self, filename, debug = False):
        self.doDebug=debug
        self.infile=filename + ".in"
        self.outfile = filename + ".out"
        self.clearOutFile()

    def clearOutFile(self):
        if os.path.exists(self.outfile):
            os.unlink(self.outfile)

    def thisFile(self):
        print(__name__)
        self.debug(__file__)

    def debug(self,*vals, **kwargs):
        if self.doDebug:
            print(*vals, **kwargs)

    def getInput(self):
        with open(self.infile,'r') as infile:
            lineNum = 0
            for line in infile:
                line=line.strip("\n ")
                yield (lineNum,line)
                lineNum += 1

    def writeOutput(self,case, out):
        with open(self.outfile, 'a') as outfile:
            outfile.write("Case #%d: %s\n" % (case,out))


def main():

    global args
    # TODO: Do something more interesting here...
    print('Hello world!')

if __name__ == '__main__':
    try:
        start_time = time.time()
        # Parser: See http://docs.python.org/dev/library/argparse.html
        parser = argparse.ArgumentParser(description='Python script')
        parser.add_argument('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_argument('-ver', '--version', action='version', version='1.0')
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

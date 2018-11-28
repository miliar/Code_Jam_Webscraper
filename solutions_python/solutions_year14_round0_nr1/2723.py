#!/usr/bin/env python
import datetime
import logging
import subprocess
import sys

from optparse import OptionParser

def solve(filename):
    lines = [line.strip() for line in open(filename)]
    num_test_cases = int(lines[0])
    lines = lines[1:]
    for num in range(num_test_cases):
        row1 = int(lines[0])
        set1 = set([int(i) for i in lines[row1].split()])
        lines = lines[5:]

        row2 = int(lines[0])
        set2 = set([int(i) for i in lines[row2].split()])
        lines = lines[5:]
        
        common = set1 & set2
        if len(common) == 1:
            logging.info("Case #%i: %i", num + 1, list(common)[0])
        elif len(common) == 0:
            logging.info("Case #%i: Volunteer cheated!", num + 1)
        else:
            logging.info("Case #%i: Bad magician!", num + 1)
        
class Usage(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

def init_logger(verbosity):
    """ Initialize the root logger """
    # Register our logging handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(verbosity)
    rootLogger = logging.getLogger('')
    rootLogger.addHandler(handler)

    # Decrease the log level of the root logger if needed
    if verbosity < rootLogger.level:
        rootLogger.setLevel(verbosity)

def main():
    """ Main loop """
    parser = OptionParser("%prog [options]")
    parser.add_option("--verbosity", type=int, action="store",
                    dest="verbosity", default=20,
                    help="verbosity of output, default is: "
                        "20 (INFO)")

    (options, args) = parser.parse_args()
    init_logger(options.verbosity)

    try:
        if len(args) < 1:
            raise Usage("not enough arguments")
        if len(args) > 1:
            raise Usage("too many arguments")

        solve(args[0])

        return 0

    except Usage, err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, parser.format_help()
        return 1

if __name__ == "__main__":
    sys.exit(main())

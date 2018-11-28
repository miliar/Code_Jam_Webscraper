#!/usr/bin/env python
import datetime
import logging
import subprocess
import sys

from optparse import OptionParser

def cookie(num, c, f, x):
    t = 0.0
    rate = 2.0
    eta_direct = t + x / rate
    eta_build_one_farm = t + c / rate + x / (rate + f)
    
    while eta_build_one_farm < eta_direct:
        t += c / rate
        rate += f
        eta_direct = t + x / rate
        eta_build_one_farm = t + c / rate + x / (rate + f)

    logging.info("Case #%i: %.7f", num, eta_direct)

def cookie_read(filename):
    lines = [line.strip() for line in open(filename)]
    num_test_cases = int(lines[0])
    lines = lines[1:]
    for num in range(num_test_cases):
        numbers = lines[0].split()
        lines = lines[1:]
        
        c = float(numbers[0])
        f = float(numbers[1])
        x = float(numbers[2])
        cookie(num + 1, c, f, x)
        
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

        cookie_read(args[0])

        return 0

    except Usage, err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, parser.format_help()
        return 1

if __name__ == "__main__":
    sys.exit(main())

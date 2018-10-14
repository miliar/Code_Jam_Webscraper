"""
Google Code Jam 2009, Round 1C, Problem A
"""
import array
import itertools
import logging
import math
from optparse import OptionParser
import os
import string
import sys


logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


ALL_DIGITS = string.digits + string.lowercase

class InvalidParameter(Exception):
    pass


class Answerer(object):
    def __init__(self, params):
        self.params = params

    def solve(self):
        self.initialize()
        self.solve_all_cases()
        self.finalize()

    def initialize(self):
        self.problem_data = {}
        self.open_input()
        self.open_output()

    def finalize(self):
        self.close_input()
        self.close_output()
        del self.problem_data

    def open_input(self):
        input_abspath = self.params["input_abspath"]
        if input_abspath:
            input = open(input_abspath, "r")
        else:
            input = sys.stdin
        self.input = input

    def close_input(self):
        assert self.input.read() == "", "unexpected input data"
        self.input.close()

    def open_output(self):
        output_abspath = self.params["output_abspath"]
        if output_abspath:
            output = open(output_abspath, "w")
        else:
            output = sys.stdout
        self.output = output

    def close_output(self):
        self.output.flush()
        self.output.close()

    def solve_all_cases(self):
        self.make_problem_data()
        for case_id in range(1, self.problem_data["n_case"] + 1):
            logger.info("solving Case #%d ...", case_id)
            self.start_case(case_id)
            self.solve_case()
            self.end_case()

    def make_problem_data(self):
        T = int(self.input.readline().rstrip("\n"))
        logger.info("T=%d", T)

        self.problem_data["n_case"] = T

    def start_case(self, case_id):
        self.case_data = {'case_id': case_id}

        self.case_data['symbols'] = self.input.readline().rstrip("\n")

    def end_case(self):
        del self.case_data

    def solve_case(self):
        symbols = self.case_data['symbols']
        all_digits = string

        translator = {}

        translator[symbols[0]] = 1

        i = 0
        for d in symbols:
            if d not in translator:
                translator[d] = i
                i += 1
                if i == 1:
                    # 1 is already used
                    i = 2

        base = len(translator.keys())
        if base == 1:
            base = 2 # they aren't using unary (base 1)
        logger.info("base=%d", base)
        logger.info("translator=%s", translator)    

        answer = 0
        for i, d in enumerate(symbols[::-1]):
            answer += translator[d] * (base ** i)

        self.output.write(
            "Case #%d: %d\n" % (self.case_data["case_id"], answer)
            )


def add_options(opt_parser):
    opt_parser.add_option("-d", "--dir",
                          dest="dir", 
                          help="base directory for <input> and <output>",
                          metavar="DIR",
                          default=None)
    opt_parser.add_option("-i", "--input",
                          dest="input", 
                          help="input file, relative path to <dir>",
                          metavar="FILE",
                          default=None)
    opt_parser.add_option("-o", "--output",
                          dest="output", 
                          help="output file, relative path to <dir>",
                          metavar="FILE",
                          default=None)
    opt_parser.add_option("-v", "--verbose",
                          dest="verbose", 
                          help="enable logging",
                          action="store_true",
                          default=False)
    return opt_parser

def get_params(options):
    params = {}
    error = []

    param_list = ["dir", "input", "output", "verbose"]

    for key in param_list:
        params[key] = getattr(options, key)

    if not params["dir"]:
        params["dir"] = os.getcwd()

    if not os.path.exists(params["dir"]):
        error.append("<%s> not found." % dir)
    else:    
        for f in ["input", "output"]:
            if not params[f]:
                params[f + "_abspath"] = None
                continue

            f_abspath = os.path.join(params["dir"], params[f])
            params[f + "_abspath"] = f_abspath
            
            if f == "output" and os.path.exists(f_abspath):
                error.append("%s already exists." % f_abspath)

    if params["verbose"]:
        logging.getLogger().setLevel(logging.DEBUG)
    else:    
        logging.getLogger().setLevel(logging.ERROR)

    if error:
        raise InvalidParameter, "\n".join(error)
    else:
        return params

def main(argv):
    """Usage: %(prog)s [options]
    """

    opt_parser = OptionParser(usage=main.__doc__ % dict(prog=__file__) + \
                                  "\nDescription: " + __doc__.strip(),
                              version="1.0")
    opt_parser = add_options(opt_parser)
    (options, args) = opt_parser.parse_args(args=argv)

    try:
        params = get_params(options)
    except InvalidParameter, e:
        logging.error(e)
        opt_parser.print_help()
        raise SystemExit
    
    logger.info("start")
    logger.info(params)
    answerer = Answerer(params)
    answerer.solve()
    logger.info("end")

if __name__ == '__main__':
    main(sys.argv)

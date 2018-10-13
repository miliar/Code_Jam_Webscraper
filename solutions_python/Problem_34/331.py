"""
Google Code Jam 2009, Qualification Round, Problem A
"""
import itertools
import math
from optparse import OptionParser
import os
import sys

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class InvalidParameter(Exception):
    pass


class PatternAnalyzer(object):
    def __init__(self, problem_data):
        self.problem_data = problem_data


    def start_analyze(self, case_data):    
        self.case_data = case_data
        self.in_parenthesis = False
        self.buf = []

    def end_analyze(self):
        del self.case_data
        del self.in_parenthesis
        del self.buf

    def analyze(self, case_data):
        self.start_analyze(case_data)
        r = self.analyze_main()
        self.end_analyze()
        return r

    def iter_token(self, pattern):
        logger.info("pattern: %s", pattern)
        for c in pattern:
            if c == "(":
                if self.buf:
                    yield self.buf
                else:
                    # in case of )(
                    pass
                self.in_parenthesis = True
            elif c == ")":
                yield self.buf
                self.buf = []
                self.in_parenthesis = False
            else:
                if self.in_parenthesis:
                    self.buf.append(c)
                else:
                    yield [c]

    def analyze_main(self):
        pattern = self.case_data["pattern"]
        heads = [""]

        for i, token in enumerate(self.iter_token(pattern)):
            d = i + 1

            new_heads = []
            for c in token:
                for h in heads:
                    new_h = h + c
                    if new_h in self.problem_data["words"][d]:
                        new_heads.append(new_h)

            if not new_heads:
                logger.info("no candidates up to head %d-th chars", i + 1)
                return 0
            heads = new_heads
            logger.info("candidates up to head %d-th chars: %s", i + 1, heads)

        return len(heads)

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

    def make_problem_data(self):
        L, D, N = map(int, self.input.readline().rstrip("\n").split(" "))
        logger.info("L=%d, D=%d, N=%d", L, D, N)

        self.problem_data["n_case"] = N

        self.problem_data["L"] = L
        self.problem_data["D"] = D
        self.problem_data["N"] = N

        logger.info("make words")
        words = []
        for i in range(D):
            w = self.input.readline().rstrip("\n")
            words.append(w)
        words = frozenset(words)
        self.problem_data["words"] = [None] # unused

        for i in range(1, L):
            logger.info("make words of %d head chars", i)
            words_head = frozenset([w[:i] for w in words])
            self.problem_data["words"].append(words_head)

        logger.info("make words of %d head chars", L)
        self.problem_data["words"].append(words)    

        # print self.problem_data["words"]
        self.analyzer = PatternAnalyzer(self.problem_data)

    def start_case(self, case_id):
        self.case_data = {'case_id': case_id}

        pattern = self.input.readline().rstrip("\n")
        self.case_data["pattern"] = pattern

    def solve_case(self):
        answer = self.analyzer.analyze(self.case_data)
        self.output.write(
            "Case #%d: %d\n" % (self.case_data["case_id"], answer)
            )

    def end_case(self):
        del self.case_data

    def solve_all_cases(self):
        self.make_problem_data()
        for case_id in range(1, self.problem_data["n_case"] + 1):
            logger.info("solving Case #%d ...", case_id)
            self.start_case(case_id)
            self.solve_case()
            self.end_case()

def add_options(opt_parser):
    opt_parser.add_option("-d", "--dir",
                          dest="dir", 
                          help="base directory for <input> and <output>",
                          metavar="DIR")
    opt_parser.add_option("-i", "--input",
                          dest="input", 
                          help="input file, relative path to <dir>",
                          metavar="FILE")
    opt_parser.add_option("-o", "--output",
                          dest="output", 
                          help="output file, relative path to <dir>",
                          metavar="FILE")
    opt_parser.add_option("-v", "--verbose",
                          dest="verbose", 
                          help="enable logging",
                          action="store_true",
                          default=False)
    return opt_parser

def get_params(options):
    params = {}
    error = []

    param_list = [
        ("dir",     None, False),
        ("input",   None, False),
        ("output",  None, False),
        ("verbose", None, False),
    ]

    for key, default, is_required in param_list:
        params[key] = getattr(options, key)

        if params[key] is None:
            params[key] = default

        if is_required is True and params[key] is None:
            error.append("<%s> is required." % key)

    if not params["dir"]:
        params["dir"] = os.getcwd()

    if not os.path.exists(params["dir"]):
        error.append("<%s> not found." % dir)
    else:    
        for f in ["input", "output"]:
            if not params[f]:
                # use sys.stdin and/or sys.stdout
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
    answerer = Answerer(params)
    answerer.solve()
    logger.info("end")

if __name__ == '__main__':
    main(sys.argv)

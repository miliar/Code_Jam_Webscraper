"""
Google Code Jam 2009, Qualification Round, Problem B
"""
import array
import itertools
import math
from optparse import OptionParser
import os
import string
import sys

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class InvalidParameter(Exception):
    pass


class Answerer(object):

    SINK = 0
    NORTH = 1
    WEST = 2
    EAST = 3
    SOUTH = 4
    
    UNASSIGNED = "0"

    def __init__(self, params):
        self.params = params
        self.neighbor_funcs = [
            (self.NORTH, self.north_index),
            (self.WEST, self.west_index),
            (self.EAST, self.east_index),
            (self.SOUTH, self.south_index),
            ]
        
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
        T = int(self.input.readline().rstrip("\n"))
        logger.info("T=%d", T)

        self.problem_data["n_case"] = T

    def coordinate_to_index(self, coordinate):
        x, y = coordinate
        return x + y * self.case_data["W"]

    def index_to_coordinate(self, index):
        x = index % self.case_data["W"]
        y = index // self.case_data["W"]
        return (x, y)

    def north_index(self, index):
        i =  index - self.case_data["W"]
        if i < 0:
            return None
        else:
            return i

    def west_index(self, index):
        i = index % self.case_data["W"]
        if i == 0:
            return None
        return index - 1

    def east_index(self, index):
        i = index % self.case_data["W"]
        if i == self.case_data["W"] - 1:
            return None
        return index + 1

    def south_index(self, index):
        i =  index + self.case_data["W"]
        if i >= self.case_data["n_index"]:
            return None
        else:
            return i

    def start_case(self, case_id):
        self.case_data = {'case_id': case_id}

        H, W = map(int, self.input.readline().rstrip("\n").split(" "))
        self.case_data["H"] = H
        self.case_data["W"] = W
        self.case_data["n_index"] = H * W
        logger.info("H=%d, W=%d", H, W)

    def solve_case(self):
        logger.info("memory allocation")
        n_index = self.case_data["n_index"]

        altitudes = array.array('i', itertools.repeat(0, n_index))
        flows = array.array('i', itertools.repeat(0, n_index))
        labels = array.array('c', itertools.repeat(self.UNASSIGNED, n_index))

        logger.info("load altitudes")
        index = 0
        for i in range(self.case_data["H"]):
            for alt in map(int, self.input.readline().rstrip("\n").split(" ")):
                altitudes[index] = alt
                index += 1

        logger.info("determine flows")
        for index in range(self.case_data["n_index"]):
            min_alt = sys.maxint
            flow_into = self.SINK
            current_alt = altitudes[index]

            # determine the lowest neighbor
            for d, func in self.neighbor_funcs:
                neighbor_index = func(index)

                if neighbor_index is not None:
                    alt = altitudes[neighbor_index]
                    if (alt < current_alt) and (alt < min_alt):
                        # if alt == current_alt, then no flow
                        # if alt == min_alt, prefer NOARTH than WEST, WEST than EAST, EAST than SOUTH
                        min_alt = alt
                        flow_into = d

            flows[index] = flow_into

            if flow_into == self.SINK:
                msg = "%s is sink with altitude %d" \
                    % (str(self.index_to_coordinate(index)), current_alt)
                logger.info(msg)

        logger.info("assign label")
        i_label = 0

        for start_index in range(self.case_data["n_index"]):
            routes = array.array('i', [])

            index = start_index
            while True:
                routes.append(index)
                flow_into = flows[index]
                if flow_into == self.SINK:
                    if labels[index] == self.UNASSIGNED:
                        label = string.ascii_lowercase[i_label]
                        i_label += 1
                    else:
                        label = labels[index]
                    break
                elif labels[index] != self.UNASSIGNED:
                    label = labels[index]
                    break

                d, func = self.neighbor_funcs[flow_into - 1] # neighbor_funcs[0] corresponds NOARTH
                index = func(index)

            logger.info("assign label %s to %s", label, routes)
            for i in routes:
                labels[i] = label

        self.output.write(
            "Case #%d:\n" % (self.case_data["case_id"])
            )

        for y in range(self.case_data["H"]):
            r = []
            for x in range(self.case_data["W"]):
                index = self.coordinate_to_index((x,y))
                r.append(labels[index])
            self.output.write(" ".join(r))
            self.output.write("\n")

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

from __future__ import division
import math
#import math
#import itertools
#import numpy as np
#import networkx as nx
#from networkx.algorithms.shortest_paths import floyd_warshall, dijkstra_path
# written by Matan Levy for codejam contest
# used python 2 at pycharm env. using pypy interpreter


class LineReader:
    """
    A class used to parse a line (i.e case) from a file
    """

    def __init__(self, file_path, line_type, delimiter=' ', **kwargs):
        self._file = file_path
        self._delimiter = ' '       # default
        self._action = lambda x: x  # default
        self.line_type = None       # default
        self.kwargs = kwargs
        self.reset_type(line_type, delimiter, **kwargs)

    def reset_type(self, line_type, delimiter=' ', **kwargs):
        self._delimiter = delimiter
        self.line_type = line_type
        self.kwargs = kwargs
        if line_type == "int":
            self._action = lambda x: int(x)
        elif line_type == "chars":
            self._action = lambda x: x
        elif line_type == "float":
            self._action = lambda x: float(x)
        elif line_type == "base_digits":
            self._action = lambda x: int(x, kwargs['base'])
        elif line_type == "words":
            self._action = lambda x: x.strip()
        elif line_type == "from_map":
            self._action = lambda x: kwargs['line_map'][x]

    def _get_line(self):
        line = self._file.readline().rstrip('\n')
        if self.line_type == "pass":
            return []
        return [self._action(x) for x in (line.split(self._delimiter)
                if self._delimiter != '' else list(line))]

    def parse_line(self):
        if 'special' not in self.kwargs:
            return self._get_line()
        line = self._get_line()
        N, K = line[0], line[1]
        pancakes = [0]*N
        for i in range(N):
            pancakes[i] = tuple(self._get_line())
        return N, K, pancakes


class ProblemsSet:
    """
    A class to represent problems data set methods (large, small and tests)
    """

    def __init__(self, set_type, in_name, act, out_name=None, print_results=False):
        """
        :param set_type: the case type (name - string)
        :param in_name: input file name (method that gets a parsed line)
        :param act - the action to run on a case
        :param out_name: output file name, none if we wish to use input file name with .in->.out
        :param print_results: true if we wish to print the results to the console instead of the output file
        """
        self.input_file_name = in_name
        self.output_file_name = str.replace(in_name, ".in", ".out") if out_name is None else out_name
        self.print_results = print_results
        self.set_type = set_type
        self.act = act


class CompSolver:
    """
    A base class for solving a generic input output problem for the contest
    """
    default_output_format = "Case #{}: {}\n"

    def __init__(self, output_format=None, line_type="int", delimiter=' ', **kwargs):
        """
        :param output_format: string format for the output case line
        :param case_type: default case type: "test", "small" or "large" (leave empty for no-op)
        :param line_type: see LineReader class: "int", "chars", "float", "base_digits", "words", "from_map"
        :param delimiter: the line delimiter ('' for splitting to chars)
        :param kwargs: additional arguments for LineReader ('base' for base conversion, and 'line_map' for mapping)
        """
        self.output_format = CompSolver.default_output_format if output_format is None else output_format
        self.line_type = line_type
        self.delimiter = delimiter
        self.kwargs = kwargs
        self.problems_sets = {}

    def set_case(self, set_type, in_name, act, out_name=None, print_results=False):
        """
        insert a new case
        """
        self.problems_sets[set_type] = ProblemsSet(set_type, in_name, act, out_name, print_results)

    def get_case(self, case):
        """
        :param case: case name
        :rtype: ProblemsSet
        """
        if case in self.problems_sets:
            return self.problems_sets[case]
        raise Exception("case not found!")

    def run(self, case_type=None):
        """
        Runs a case type - test, small or large
        :param case_type: use if we want to run a different case than the default one which is given at the class
                            constructor
        """
        case = self.get_case(case_type)

        with open(case.input_file_name, 'r') as in_file:
            reader = LineReader(in_file, "int")
            case_count = reader.parse_line()[0]
            with open(case.output_file_name, 'w') as out_file:
                reader.reset_type(self.line_type, self.delimiter, **self.kwargs)
                for i in range(case_count):
                    case_input = reader.parse_line()
                    result = case.act(case_input)
                    #output = self.default_output_format.format(i+1, result)
                    output = "Case #"+ str(i+1) + (": %.8f\n" % result)
                    if case.print_results:
                        print(output)
                    else:
                        out_file.write(output)


def solve_small(case):
    N, K, pancakes = case
    # 2, 1, [(100, 20), (200, 10)]
    pancakes.sort(key=lambda x: -x[0])
    curr_max = 0
    for i in range(N-K+1):
        # start from pancake number i
        a = [x[0]*x[1] for x in pancakes[i+1:]]
        a.sort(key=lambda x: -x)
        a = a[0:K-1]
        result = math.pi * (pancakes[i][0])**2 + (sum(a)+pancakes[i][0]*pancakes[i][1])*math.pi*2
        if result > curr_max:
            curr_max = result
    return curr_max


test1 = CompSolver(line_type="int", delimiter=' ', special=True)
test1.set_case("small", 'A-large.in', solve_small, print_results=False)
test1.run("small")

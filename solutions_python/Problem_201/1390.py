#import math
#import itertools
#import numpy as np
import math
import heapq

# written by Matan Levy for codejam contest
# used python 3 at pycharm env.


class LineReader:
    """
    A class used to parse a line (i.e case) from a file
    """

    def __init__(self, file, line_type, delimiter=' ', **kwargs):
        self._file = file
        self._delimiter = ' '       # default
        self._action = lambda x: x  # default
        self.line_type = None       # default
        self.reset_type(line_type, delimiter, **kwargs)

    def reset_type(self, line_type, delimiter=' ', **kwargs):
        self._delimiter = delimiter
        self.line_type = line_type
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

    def parse_line(self):
        line = self._file.readline().rstrip('\n')
        if self.line_type == "pass":
            return []

        return [self._action(x) for x in (line.split(self._delimiter)
                if self._delimiter != '' else list(line))]


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
                    output = self.default_output_format.format(i+1, result)
                    if case.print_results:
                        print(output)
                    else:
                        out_file.write(output)


# used max heap implementation from:
# http://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
class MaxHeapObj(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


class MinHeap(object):
    def __init__(self):
        self.h = []

    def heappush(self, x):
        heapq.heappush(self.h, x)

    def heappop(self):
        return heapq.heappop(self.h)

    def __getitem__(self, i):
        return self.h[i]

    def __len__(self):
        return len(self.h)


class MaxHeap(MinHeap):
    def heappush(self, x):
        heapq.heappush(self.h, MaxHeapObj(x))

    def heappop(self):
        return heapq.heappop(self.h).val

    def __getitem__(self, i):
        return self.h[i].val


def solve1(case):
    n = case[0]
    k = case[1]
    heap = MaxHeap()
    heap.heappush(n)
    for i in range(k-1):
        x = heap.heappop()
        if x == 2:
            heap.heappush(1)
        if x > 2:
            if x % 2 == 0:
                heap.heappush(int(x//2))
                heap.heappush(int(x//2) - 1)
            else:
                heap.heappush(int(x//2))
                heap.heappush(int(x//2))
    item = heap.heappop()
    if item % 2 == 0:
        return "{} {}".format(int(item//2), int(item//2) - 1)
    return "{} {}".format(int(item//2), int(item//2))


def calc(n, k):
    if k == 1:
        if n % 2 == 0:
            return int(n//2), int(n//2 - 1)
        return int(n//2), int(n//2)
    # k > 1
    if n % 2 == 1:
        next_n = int(n//2)
        if k % 4 in [1, 2]:
            next_n += 1
        return calc(next_n, int(math.floor(k//2)))
    else:
        new_k = 1
        if k > 3:
            new_k = int(k//2) + k % 2
        return calc(int(n//2), new_k)



def rec_sol(case):
    n = case[0]
    k = case[1]
    return ' '.join(str(x) for x in calc(n, k))

main_dict = {}

def create_key(n, k):
    if n % 2 == 0:
        left_size = int(n//2) - 1
        right_size = int(n//2)
    else:
        left_size = int(n//2)
        right_size = int(n//2)
    main_dict[(n,k)] = main_dict()


def build_table(N):
    for n in range(1, N+1):
        for k in range(1, n+1):
            create_key(n, k)

##################################################################################
main_map = {}
leaves = -1, -1
leaves2 = -1


def find_level_items(num, level):
    global leaves, leaves2
    if (num, level) in main_map:
        return main_map[(num, level)]

    if level == 1:
        if num % 2 == 0:
            result = 1
            leaves = int(num//2), int(num//2) - 1
        else:
            leaves2 = int(num//2)
            result = 0
        main_map.update({(num, level): result})
        return result

    right = find_level_items(int(num//2), level-1)
    if num % 2 == 0:
        left = find_level_items(int(num//2) - 1, level-1)
    else:
        left = find_level_items(int(num//2), level-1)

    main_map.update({(num, level): left + right})
    return left + right


def get_x(num, level):
    return int(num//(2**level))


def get_level(k):
    return math.floor(math.log2(k))


def get_end_space(num, k):
    if k == 1:
        return num
    level = get_level(k)
    leave_count = find_level_items(num, level)
    counted_max = True
    if leaves[0] != -1:
        x = max(leaves)
        if x == leaves2:
            counted_max = False
    else:
        return leaves2
    if counted_max:
        level_x_count = leave_count
        diff = k-2**level
    else:
        level_x_minus_one_count = leave_count
        diff = k-2**level
        level_x_count = 2**level - level_x_minus_one_count
    level_x_count -= diff
    if level_x_count > 0:
        return x
    return x-1


def get_space_info(num, k):
    global leaves2, leaves, main_map
    main_map = {}

    leaves = -1, -1
    leaves2 = -1
    space = get_end_space(num, k)

    if space % 2 == 1:
        return int(space//2), int(space//2)
    return int(space//2), int(space//2)-1


def tree_solve(case):
    n = case[0]
    k = case[1]
    return ' '.join(str(x) for x in get_space_info(n, k))
#################################################################################

#import timeit
#start = timeit.default_timer()
test1 = CompSolver(line_type="int", delimiter=' ')
#test1.set_case("rec", 'test2.in', rec_sol, out_name='rec.out', print_results=False)
#test1.set_case("test", 'test2.in', solve1, print_results=False)
#test1.set_case("small1", 'test5.in', solve1, print_results=False)
test1.set_case("tree", 'C-small-2-attempt0.in', tree_solve, print_results=False)
#test1.run("small1")
test1.run("tree")
#test1.run("test")
#test1.run("rec")
#stop = timeit.default_timer()
#print(stop-start)
import functools
import sys
import multiprocessing

POOL_SIZE = 8


def by_first(inp):
    tot = 0
    prev = 0
    for v in inp:
        if v < prev:
            tot += (prev - v)
        prev = v
    return tot


def by_second(inp):
    prev = 0
    max_diff = 0
    for v in inp:
        if v < prev:
            max_diff = max(max_diff, (prev - v))
        prev = v

    tot = 0
    for v in inp[:-1]:
        tot += min(max_diff, v)

    return tot


def mush(inp):
    inp = map(int, inp)
    return str(by_first(inp)) + ' ' + str(by_second(inp))


def parse_inputs(inp):
    test_cases = int(inp[0].strip())
    inps = []
    for t in range(test_cases):
        m = inp[t*2+2].strip().split()
        inps.append(m)
    return inps


def read_input_lines(fname):
    """Reads file and returns the a list of lines.

    Args:
        fname: String, file path.

    Returns:
        The number of test cases and a list of lines.
    """
    lines = []
    with open(fname, 'r') as fin:
        lines = fin.readlines()
    return lines


def get_input_file_name():
    """Returns the input file name passed as cmd arg.

    Returns:
        A string, the path of the input file.
    """
    return sys.argv[1]


def process_test_cases(inp_list, parse_func, exec_func):
    """Processes test cases in parallel.

    Args:
        inp_list: The list of input lines.
        parse_func: A function which gets the test case data.
        exec_func: A function which executes a single test case.

    Returns:
        A list of lines - the output that is to be printed.
    """
    pool = multiprocessing.Pool(POOL_SIZE)
    return pool.map(exec_func, parse_func(inp_list))


def print_output(op_list):
    """Prints the output in the correct format.

    Args:
        op_list: The list of output data.
    """
    for i, op_data in enumerate(op_list):
        print "Case #" + str(i+1) + ":", str(op_data)


def main(parse_func, exec_func):
    """Executes the whole thing.

    Args:
        parse_func: A func obj to parse the input data.
        exec_func: A func obj to execute a single test case.
    """
    print_output(
        process_test_cases(
            read_input_lines(get_input_file_name()),
            parse_func, exec_func))


if __name__ == '__main__':
    main(parse_inputs, mush)

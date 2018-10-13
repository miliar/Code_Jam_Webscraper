import functools
import sys
import multiprocessing


POOL_SIZE = 8


def debug_dec(fn):
    """Use for debugging.

    Args:
        fn: The func to be debugged.

    Returns:
        Decorated func which prints args and result.
    """
    @functools.wraps(fn)
    def inner_func(*args, **kwargs):
        print '-' * 20
        print fn.__name__
        print args, kwargs
        ret_val = fn(*args, **kwargs)
        print ret_val
        print '-' * 20
        return ret_val

    return inner_func

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
    return lines[1:]


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


def umain(parse_func, exec_func):
    """Executes the whole thing.

    Args:
        parse_func: A func obj to parse the input data.
        exec_func: A func obj to execute a single test case.
    """
    print_output(
        process_test_cases(
            read_input_lines(get_input_file_name()),
            parse_func, exec_func))



def parse_line(line):
    """Parses a single line for data.

    Args:
        line: A string containing data for one line.

    Returns:
        A dict containing the data parsed.
    """
    data = line.split()[1:][0]
    return {i: int(x) for i, x in enumerate(data)}


def parse_func(inp_list):
    """Parses the input list for test case data.

    Args:
        inp_list: A list of lines containing the input data.

    Returns:
        A list of dicts.
    """
    return [parse_line(line) for line in inp_list]


def get_needed_standing(shyness, tot_standing, is_needed):
    """Gets number of ppl that need to be added.

    Args:
        shyness: The level of shyness.
        tot_standing: The number of ppl already standing.
        is_needed: A boolean to indicate whether ppl are there
                   at this shyness level or not.

    Returns:
        The number of ppl who need to be added.
    """
    return (
        shyness - tot_standing
        if is_needed and shyness >= tot_standing else 0)


def exec_func(inp_dict):
    """Works on input for a single test case.

    Args:
        inp_dict: A dict, shyness level mapped to num of ppl.

    Returns:
        The output as required.
    """
    tot_needed = tot_standing = 0

    for key in sorted(inp_dict.keys()):
        needed = get_needed_standing(
            key, tot_standing, inp_dict[key] > 0)
        tot_needed += needed
        tot_standing += needed + inp_dict[key]

    return str(tot_needed)


def main():
    """Passes the custom funcs to the main func in utils."""
    umain(parse_func, exec_func)

if __name__ == '__main__':
    main()

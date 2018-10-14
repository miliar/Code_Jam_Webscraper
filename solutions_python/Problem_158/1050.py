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


def parse_func(inp_list):
    result_list = []
    for line1 in inp_list:
        line = line1.split()
        result_list.append(
            (int(line[0]), int(line[1]), int(line[2])))
    return result_list


def exec_func(inp_tuple):
    X, R, C = inp_tuple
    can_place = False
    if R * C % X > 0:
        can_place = False
    elif X >= 4:
        if R == 4 and C == 4:
            can_place = True
        if R == 4 and C == 3:
            can_place = True
        if R == 3 and C == 4:
            can_place = True
        if R < 3 and C < 3:
            can_place = False
    elif X == 3:
        if R == 4 and C == 4:
            can_place = False
        elif R == 4 and C == 3:
            can_place = True
        elif R == 4 and C == 2:
            can_place = False
        elif R == 4 and C == 1:
            can_place = True
        elif R == 3 and C == 4:
            can_place = True
        elif R == 2 and C == 4:
            can_place = False
        elif R == 1 and C == 4:
            can_place = True
        elif R == 3 and C == 3:
            can_place = True
        elif R == 3 and C == 2:
            can_place = True
        elif R == 3 and C == 1:
            can_place = False
        elif R == 2 and C == 3:
            can_place = True
        elif R == 1 and C == 3:
            can_place = False
        elif R < 3 and C < 3:
            can_place = False

    elif X == 2:
        if R == 4 and C == 4:
            can_place = True
        elif R == 4 and C == 3:
            can_place = True
        elif R == 4 and C == 2:
            can_place = True
        elif R == 4 and C == 1:
            can_place = True
        elif R == 3 and C == 4:
            can_place = True
        elif R == 2 and C == 4:
            can_place = True
        elif R == 1 and C == 4:
            can_place = True
        elif R == 3 and C == 3:
            can_place = False
        elif R == 3 and C == 2:
            can_place = True
        elif R == 3 and C == 1:
            can_place = False
        elif R == 2 and C == 3:
            can_place = True
        elif R == 1 and C == 3:
            can_place = False
        elif R == 2 and C == 2:
            can_place = True
        elif R == 1 and C == 2:
            can_place = True
        elif R == 2 and C == 1:
            can_place = True
        elif R < 2 and C < 2:
            can_place = False
    elif X == 1:
        can_place = True

    ret_val = "GABRIEL" if can_place else "RICHARD"
    return ret_val


def main2():
    main(parse_func, exec_func)


if __name__ == "__main__":
    main2()

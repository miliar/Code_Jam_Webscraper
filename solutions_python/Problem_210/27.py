###############################################################################
#      Coded by Hai Brenner (Israel) for the Google Code Jam Competition      #
###############################################################################

from functools import wraps, update_wrapper
import time
import os

###############################
#      useful decorators
###############################


class DecoratedFunctionInfo:

    def __init__(self):
        self.memoization_registry_reset_on_new_test_case = []
        self.function_counters = {}

    def reset_memoization_on_new_test_case(self):
        for cache_d in self.memoization_registry_reset_on_new_test_case:
            cache_d.clear()

    def get_function_counters(self):
        return self.function_counters


_GLOBAL_DECORATED_FUNCTIONS_INFO = DecoratedFunctionInfo()


# a decorator for memoizing function outputs
def memoize_it(reset_on_new_test_case=False):
    cache = {}
    if reset_on_new_test_case:
        _GLOBAL_DECORATED_FUNCTIONS_INFO.memoization_registry_reset_on_new_test_case.append(cache)

    def real_decorator(function):
        def wrapper(*args, **kwargs):
            if args not in cache:
                cache[args] = function(*args, **kwargs)
            return cache[args]
        return update_wrapper(wrapper, function)
    return real_decorator


# a decorator to add time benchmarking for a function
def time_it(inner_func):
    @wraps(inner_func)
    def wrapper(*args, **kwargs):
        print('--> Start function \'' + inner_func.__qualname__ + '\' : ', time.ctime())
        start_time = time.time()
        res = inner_func(*args, **kwargs)
        end_time = time.time()
        print('--> End   function \'' + inner_func.__qualname__ + '\' : ', time.ctime())
        print('--> Elapsed time \'' + inner_func.__qualname__ + '\' : ', end_time-start_time)
        print()
        return res
    return wrapper


# a decorator for logging the function's inputs and outputs
def log_it(arguments=True, output=True):
    def decorating_function(user_function):
        def wrapper(*args, **kwargs):
            if arguments:
                print(time.ctime(),
                      ': function \'' + user_function.__qualname__ + '\' arguments args=', args, 'kwargs=', kwargs)
            result = user_function(*args, **kwargs)
            if output:
                print(time.ctime(), ': function \'' + user_function.__qualname__ + '\' outputs ', result)
            return result
        return update_wrapper(wrapper, user_function)
    return decorating_function

        
# a decorator for counting the number of calls to the wrapped function
def count_it(inner_func):
    func_counters = _GLOBAL_DECORATED_FUNCTIONS_INFO.function_counters
    assert type(func_counters) == dict
    assert inner_func.__qualname__ not in func_counters
    func_counters[inner_func.__qualname__] = 0

    @wraps(inner_func)
    def wrapper(*args, **kwargs):
        global func_counters
        func_counters[inner_func.__qualname__] += 1
        return inner_func(*args, **kwargs)
    return wrapper


# a decorator for pre-processing the function and automatically save the result
def pre_process_it(inner_func):
    import inspect
    import pickle
    a = inspect.signature(inner_func)
    if len(a.aparmeters):
        raise ValueError('A pre process function must not have arguments')

    # noinspection PyUnusedLocal
    @time_it
    @wraps(inner_func)
    def wrapper(*args, **kwargs):
        filename = 'pre-process_' + inner_func.__qualname__ + '.pickle'
        # noinspection PyArgumentList
        if filename not in os.listdir():
            print('--> Pre process started for function \'' + inner_func.__qualname__ + '\' ....')
            pre_process_data = inner_func()
            print('--> Pre process ended for function \'' + inner_func.__qualname__ + '\'')
            print('--> Pickling started for function \'' + inner_func.__qualname__ + '\' ....')
            with open(filename, 'wb') as f_pp:
                pickle.dump(pre_process_data, f_pp, pickle.HIGHEST_PROTOCOL)
            print('--> Pickling ended for function \'' + inner_func.__qualname__ + '\'')
        print('--> Unpickling pre-processed data of function \'' + inner_func.__qualname__ + '\' ...')
        with open(filename, 'rb') as f_pp:
            data = pickle.load(f_pp)
        print('--> Unpickling ended')
        print()
        return data

    return wrapper
 

###########################################
# automatic runner
###########################################

# a class to wrap automatically the IO files in one class
# noinspection PyPep8Naming
class GCJIOWrapper:

    def __init__(self, input_filename, parsed_filename, output_filename):
        self.__input_filename = input_filename
        self.__parsed_filename = parsed_filename
        self.__output_filename = output_filename
        self.__index_test_case = 0
        self.__input_file = None
        self.__parsed_file = None
        self.__output_file = None

    def __enter__(self):
        # open the IO files
        self.__input_file = open(self.__input_filename, 'r')
        self.__parsed_file = open(self.__parsed_filename, 'w')
        self.__output_file = open(self.__output_filename, 'w')

    # noinspection PyUnusedLocal
    def __exit__(self, type_e, value, tb):
        # close the IO files
        self.__input_file.close()
        self.__parsed_file.close()
        self.__output_file.close()

    def readline(self):
        # read one line from the input. write it as is to the parsed file
        l = self.__input_file.readline()
        self.__parsed_file.write(l)
        return l
    
    def new_test_case(self):
        # mark a new test case to the parsed file
        self.__index_test_case += 1
        self.__parsed_file.write('\n## _BigOnion Test case: ' + str(self.__index_test_case) + ' ##\n')
    
    def write(self, s):
        # write to the output file
        self.__output_file.write(s)
    
    def get_test_case(self):
        # return the index of the current test case
        return self.__index_test_case
        

# This is the automatic runner    
@time_it
def main_run():
        
    # find the most current input file (.in) which is in the working directory 
    print('Directory : ', os.getcwd())
    # noinspection PyArgumentList
    file_names = [x for x in os.listdir()]
    l1 = [(os.stat(x).st_mtime, x) for x in file_names if x.endswith('.in')]
    if not l1:
        raise ValueError('No input file found')
    chosen_prefix = sorted(l1)[-1][1][:-3]
    input_filename = chosen_prefix + '.in'
    print('Chosen Input : ', input_filename)
    
    # filename of the file into which to parse the input file
    parsed_filename = chosen_prefix + '.parsed.txt'

    # filename of the output file. It has the same prefix, 
    # and it doesn't tread over the previous output file from previous attempts
    l2 = [x.split('.')[0] for x in file_names if x.endswith('.out') and x.startswith(chosen_prefix)]
    l2 = [int(x.split('-run')[-1]) for x in l2]
    output_file_index = ('000' + str(max([0] + l2) + 1))[-3:]
    output_filename = chosen_prefix + '-run' + output_file_index + '.out'
    print('Chosen Output : ', output_filename)
    print()
    
    io_wrapper = GCJIOWrapper(input_filename, parsed_filename, output_filename)
    with io_wrapper:
        solve_all_cases(io_wrapper)

    # print the chosen files once again for easy checking of correctness
    print()
    print('Conclusion :')
    print('Directory : ', os.getcwd())
    print('Chosen Input : ', input_filename)
    print('Chosen Output : ', output_filename)


# the automatic solver. Handles the test case mechanism
@time_it
def solve_all_cases(io_wrapper):
    # noinspection PyPep8Naming
    T = int(io_wrapper.readline())
    for test_case in range(1, T+1):
        io_wrapper.new_test_case()
        assert io_wrapper.get_test_case() == test_case
        _GLOBAL_DECORATED_FUNCTIONS_INFO.reset_memoization_on_new_test_case()
        solve_one_case(io_wrapper)


###########################################
# write code here
###########################################


EMPTY = '?'
CAMERON = 'c'
JAMIE = 'j'
BOTH = 'b'

VALUES = {CAMERON: 1, JAMIE: 1, BOTH: 2000}

def get_empty_sequences(full_day_time_table):
    assert full_day_time_table[0] != EMPTY
    l = full_day_time_table + [full_day_time_table[0]]
    empty_seqs = []
    i = 0
    while i < 1441:
        if l[i] != EMPTY:
            i += 1
            continue
        else:
            start = i
            start_color = l[i-1]
            assert start_color != EMPTY
            while l[i] == EMPTY:
                i += 1
            end = i
            end_color = l[end]
            if start_color != end_color:
                color = BOTH
            else:
                color = start_color
            empty_seqs.append([end-start, start, end, color])
    return empty_seqs


def fill_in_time_table(full_day_time_table):
    if full_day_time_table.count(EMPTY) == len(full_day_time_table):
        for i in range(12*60):
            full_day_time_table[i] = CAMERON
        for i in range(12 * 60, 24*60):
            full_day_time_table[i] = JAMIE
        return [CAMERON] * (12 * 60) + [JAMIE] * (12 * 60)

    while full_day_time_table[0] == EMPTY:
        del full_day_time_table[0]
        full_day_time_table.append(EMPTY)

    empty_seqs = get_empty_sequences(full_day_time_table)
    empty_seqs.sort(key=lambda x:VALUES[x[3]]*x[0])

    c_counter = full_day_time_table.count(CAMERON)
    j_counter = full_day_time_table.count(JAMIE)
    while c_counter != 720 and j_counter != 720:
        next_empty_seq = empty_seqs[0]
        if next_empty_seq[0] == 0:
            del empty_seqs[0]
        else:
            length, start, end, color = next_empty_seq
            full_day_time_table[start] = color
            if color == BOTH:
                assert full_day_time_table[start - 1] in [CAMERON, JAMIE]
                color = full_day_time_table[start - 1]
            if color == CAMERON:
                full_day_time_table[start] = CAMERON
                c_counter += 1
            elif color == JAMIE:
                full_day_time_table[start] = JAMIE
                j_counter += 1
            else:
                raise ValueError()

            empty_seqs[0][0] -= 1
            empty_seqs[0][1] += 1

    assert full_day_time_table.count(CAMERON) <= 720 and full_day_time_table.count(JAMIE) <= 720
    assert full_day_time_table.count(CAMERON) == 720 or full_day_time_table.count(JAMIE) == 720
    if full_day_time_table.count(JAMIE) == 720:
        for i in range(len(full_day_time_table)):
            if full_day_time_table[i] == EMPTY:
                full_day_time_table[i] = CAMERON
    if full_day_time_table.count(CAMERON) == 720:
        for i in range(len(full_day_time_table)):
            if full_day_time_table[i] == EMPTY:
                full_day_time_table[i] = JAMIE
    assert full_day_time_table.count(CAMERON) == 720 and full_day_time_table.count(JAMIE) == 720
    return full_day_time_table


def count_swaps(full_day_timetable):
    full_day_timetable = full_day_timetable + [full_day_timetable[0]]
    counter = 0
    for i in range(1, len(full_day_timetable)):
        if full_day_timetable[i] != full_day_timetable[i-1]:
            counter += 1
    return counter


def solve_one_case(io_wrapper):
    A_c, A_j = [int(x) for x in io_wrapper.readline().split()]

    full_day_time_table = [EMPTY] * (24*60)

    for i in range(A_c):
        start, end = [int(x) for x in io_wrapper.readline().split()]
        assert start < end
        assert end <= 24 * 60
        for m in range(start, end):
            full_day_time_table[m] = CAMERON

    for i in range(A_j):
        start, end = [int(x) for x in io_wrapper.readline().split()]
        assert start < end
        assert end <= 24 * 60
        for m in range(start, end):
            full_day_time_table[m] = JAMIE

    full_day_time_table = fill_in_time_table(full_day_time_table)
    solution = count_swaps(full_day_time_table)
    io_wrapper.write('Case #' + str(io_wrapper.get_test_case()) + ': ' + str(solution) + '\n')






main_run()

##############################################################
# utility functions meant for use in Google Code Jam solutions
# (short for jamUtils.py)
##############################################################

import time

DOWNLOAD_FILEPATH = "/Users/dkmita/Downloads/"
SMALL_FILE_ENDING = "-small-attempt"
LARGE_FILE_ENDING = "-large.in"
CAST_PRIORITY = [int, float]
SPLIT_CHAR = ' '


def attempt_cast(string):
    for cast in CAST_PRIORITY:
        try:
            return cast(string)
        except:
            pass
    return string


def gint(f):
    return int(f.readline())


def gints(f):
    return map(int, f.readline().split())


def gstrs(f):
    return f.readline()[:-1].split()


def gstr(f):
    return f.readline()[:-1]


def parse_line(line, row_num, cast):
    if SPLIT_CHAR not in line:
        return attempt_cast(line) if cast else line
    else:
        split_line = line.split(' ')
        return map(attempt_cast,split_line) if cast else split_line


def parse_lines(filename, parse=True, cast=True):
    f = open(filename, 'r')
    num_instances = 0
    lines = []
    for line in f:
        if num_instances == 0:
            num_instances = int(line)
        else:
            lines += [parse_line(1, line, cast) if parse else line[:-1]]
    assert num_instances == len(lines), "ERROR: length of input inconsistency; " \
                                        + str(num_instances) + " " + str(len(lines))
    return lines


def parse_custom(filename, rows_per_inst, parse=True, cast=True):
    f = open(filename, 'r')
    num_instances = 0
    result = []
    row_count = 0
    instance = []
    for line in f:
        if num_instances == 0:
            num_instances = int(line)
            continue
        row_count += 1
        if row_count > rows_per_inst:
            result += [instance]
            instance = []
            row_count = 1
        instance += [parse_line(line, row_count, cast) if parse else line]
    result += [instance]
    assert num_instances == len(result), "ERROR: length of input inconsistency; " \
                                         + str(num_instances) + " " + str(len(result))
    return result


def generate_output_file(input_filename, output):
    f = open(generate_output_filename(input_filename), 'w')
    for i in range(len(output)):
        instance_output_str = "case #" + str(i+1) + ": "
        instance_output = output[i]
        if isinstance(instance_output, list):
            for arg in instance_output:
                instance_output_str += str(arg) + " "
        else:
            instance_output_str += str(instance_output)
        instance_output_str += "\n"
        if i < 8:
            print instance_output_str
        f.write(instance_output_str)
    f.close()


def generate_output_filename(input_filename):
    return input_filename.split('.')[0] + ".out"


def run_solution(solution, problem_id, small_attempt, large_attempt,  test=None):
    small_file_name = DOWNLOAD_FILEPATH + problem_id + SMALL_FILE_ENDING + small_attempt + ".in"
    large_file_name = DOWNLOAD_FILEPATH + problem_id + LARGE_FILE_ENDING
    if test == "s":
        solution(small_file_name)
    elif test == "l":
        solution(large_file_name)
    elif not test:
        for filename in [small_file_name, large_file_name]:
            start_time = time.time()
            print "\n", filename
            print "====================================\n"
            solution(filename)
            print "\n", "Took", str(round(time.time()-start_time,4)) + "s", "\n"
    else:
        assert False, "ERROR: invalid test type; Use 's' or 'l'"

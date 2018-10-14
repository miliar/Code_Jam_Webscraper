"""
Problem A. Standing Ovation

It's opening night at the opera, and your friend is the prima donna (the lead female singer). You will not be in the
audience, but you want to make sure she receives a standing ovation -- with every audience member standing up and
clapping their hands for her.

Initially, the entire audience is seated. Everyone in the audience has a shyness level. An audience member with shyness
level Si will wait until at least Si other audience members have already stood up to clap, and if so, she will
immediately stand up and clap. If Si = 0, then the audience member will always stand up and clap immediately,
regardless of what anyone else does. For example, an audience member with Si = 2 will be seated at the beginning, but
will stand up to clap later after she sees at least two other people standing and clapping.

You know the shyness level of everyone in the audience, and you are prepared to invite additional friends of the
prima donna to be in the audience to ensure that everyone in the crowd stands up and claps in the end. Each of these
friends may have any shyness value that you wish, not necessarily the same. What is the minimum number of friends that
you need to invite to guarantee a standing ovation?


Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with
Smax, the maximum shyness level of the shyest person in the audience, followed by a string of Smax + 1 single digits.
The kth digit of this string (counting starting from 0) represents how many people in the audience have shyness
level k. For example, the string "409" would mean that there were four audience members with Si = 0 and nine audience
members with Si = 2 (and none with Si = 1 or any other value). Note that there will initially always be between
0 and 9 people with each shyness level.

The string will never end in a 0. Note that this implies that there will always be at least one person in the audience.

Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y
is the minimum number of friends you must invite.
"""
import os

def get_input_file_name(data_location, name):
    return os.path.join(data_location, "{}.in".format(name))

def get_output_file_name(data_location, name):
    return os.path.join(data_location, "{}.out".format(name))

def load_data_set(file_name):
    f = open(file_name, 'r')
    data = f.read().split("\n")[:-1]
    case_lines = data[1:]
    cases = []
    for case_line in case_lines:
        split_case = case_line.split(" ")
        s_max = int(split_case[0])
        shyness_list = [int(k) for k in split_case[1]]
        cases.append([s_max, shyness_list])
    return cases


def generate_result_file(results_list, file_name=None):
    """
    Takes a list of results and formats it into the Google Code Jam format.

    Takes a list of results and formats it into the Google Code Jam format. If a file name is supplied then it saves
    the string to the file.

    :param results_list: list of results
    :type results_list: list
    :param file_name: name of the file to write to
    :type file_name: str
    :return: The formatted results string
    :rtype: str
    """
    result_strings = []
    for i in range(len(results_list)):
        result_strings.append("Case #{}: {}".format(i+1, results_list[i]))
    result = "\n".join(result_strings)
    if file_name:
        f = open(file_name, 'w+')
        f.write(result)
    return result


def solve_problem(case):
    print "Case: ", case
    extras_needed = 0
    cumulative_audience = 0
    for shyness_level, k in enumerate(case[1]):
        if k is not 0 and cumulative_audience + extras_needed < shyness_level:
            extras_needed = shyness_level - cumulative_audience
        cumulative_audience += k
    print "Result: ", extras_needed
    return extras_needed


if __name__ == '__main__':
    data_location = 'data_sets'
    data_name = 'A-large'
    cases = load_data_set(get_input_file_name(data_location, data_name))
    results_arr = [solve_problem(c) for c in cases]
    print generate_result_file(results_arr, get_output_file_name(data_location, data_name))

from functools import reduce
from sys import stdin

file = stdin

def read_line():
    return file.readline().strip()


def read_int():
    return int(read_line())


def string_list_to_int_list(x):
    return [int(e) for e in x]

cases = read_int()

for case in range(cases):
    [smax, smax_string] = read_line().split(" ")
    s_list = list(map(int, list(smax_string)))
    previous = 0
    cdf = []
    for s in s_list:
        cdf.append(previous)
        previous = previous + s

    tuples = zip(range(len(s_list)), s_list, cdf)
    tuples = list(filter(lambda x: x[1] > 0, tuples))
    added = 0
    required = []
    for tuple in tuples:
        diff = max(tuple[0] - tuple[2] - added, 0)
        added = added + diff
        required.append(diff)
    accumulate = reduce(lambda a, b: a + b, required, 0)
    print("Case #" + str(case+1) + ": " + str(accumulate))

from codejam import *

def read_file(f):
    case = read_string_list(f)
    return case

def solver(case):
    num = int(case[0])
    lst = list(map(int,case[1]))
    threshold = 0
    friend = 0
    for i in range(num + 1):
        if lst[i]:
            if threshold < i:
                diff = (i - threshold)
                friend += diff
                threshold += diff
            threshold += lst[i]
    return friend

solve('A-large', read_file, solver)

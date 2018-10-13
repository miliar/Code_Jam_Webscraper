#!/usr/bin/env python2

from multiprocessing import Pool

class Problem(object):

    def __init__(self):
        pass

def debug(s, color=None):
    #from termcolor import cprint
    #cprint("[DEBUG] %s" % s, color)
    pass

def solve(problem):
    black_list = set()
    cnt = 1
    for row in problem.grid1:
        if cnt != problem.answer1:
            for n in row:
                black_list.add(n)
        cnt = cnt + 1

    candidates = set()
    for n in problem.grid2[problem.answer2 - 1]:
        if n not in black_list:
            candidates.add(n)
    l = len(candidates)
    if l == 1:
        return list(candidates)[0]
    if l > 1:
        return "Bad magician!"
    if l == 0:
        return "Volunteer cheated!"


def read_grid():
    result = []
    for i in xrange(4):
        row = map(int, raw_input().split())
        result.append(row)
    return result


if __name__ == "__main__":
    results = []
    pool = Pool()

    # read in number of cases
    cases = int(raw_input())
    for c in xrange(cases):
        # read in misc problem constants

        # read in data
        problem = Problem()
        problem.answer1 = int(raw_input())
        problem.grid1 = read_grid()
        problem.answer2 = int(raw_input())
        problem.grid2 = read_grid()

        # problem solving logic here
        results.append((c+1, pool.apply_async(solve, args=(problem, ))))

    pool.close()
    pool.join()

    for case_no, result in results:
        solution = result.get()
        # output answer
        print "Case #%d: %s" % (case_no, solution)



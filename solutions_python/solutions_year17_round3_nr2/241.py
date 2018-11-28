import os
import sys
import pandas as np
from pandas import Series, DataFrame
import numpy as np
from scipy.optimize import bisect

def solve_naive(NAc, Naj, schedule):
    if NAc <= 1 and Naj <= 1:
        return 2
    quota = 720
    schedule = DataFrame(schedule)
    schedule.sort_values('begin', inplace = 1)
    schedule['duration'] = schedule['end'] - schedule['begin']
    quota -= schedule['duration'].sum()
    intevals = []
    tmp = schedule['begin'].iloc[0] + 1440 - schedule['end'].iloc[-1]
    intevals.append(tmp)
    intevals.append(schedule['begin'].iloc[-1] - schedule['end'].iloc[0])
    if min(intevals) <= quota:
        return 2
    return 4

def solve(NAc, NAj, schedule):
    if NAc <= 2 and NAj <= 2 and NAc + NAj <= 2:
        return solve_naive(NAc, NAj, schedule)
    else:
        return -1
    #schedule = DataFrame(schedule)
    #schedule.sort_values('begin', inplace = 1)
    #schedule['tmp'] = schedule['begin'].shift(-1)
    ##schedule['duration'] = schedule['end'] - schedule['begin']
    #print(schedule)
    #return 0

if __name__ == '__main__':
    try:
        input = sys.argv[1]
    except:
        input = os.path.join('data', 'input.txt')
    basename, _ = os.path.splitext(input)
    output = basename + '.output'
    with open(input, 'r') as fin:
        with open(output, 'w') as fout:
            num_cases = int(fin.readline())
            for case in range(num_cases):
                fout.write('Case #%d: ' % (case+1))
                line = fin.readline().split(' ')
                NAc = int(line[0])
                NAj = int(line[1])
                schedule = []
                for i in range(NAc):
                    line = fin.readline().split(' ')
                    begin = int(line[0])
                    end = int(line[1])
                    schedule.append({'begin': begin, 'end': end, 'type': 1})
                for i in range(NAj):
                    line = fin.readline().split(' ')
                    begin = int(line[0])
                    end = int(line[1])
                    schedule.append({'begin': begin, 'end': end, 'type': -1})
                res = solve(NAc, NAj, schedule)
                fout.write('%d\n' % res)

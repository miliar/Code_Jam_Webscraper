import pdb
import copy
from sets import Set as set

memo = {}

def case_convert(x):
    y = [0]*9
    for i in x:
        y[i-1] += 1
    return tuple(y)
        

def solve_sub(ln, time):
    ln_conv = case_convert(ln)
    if ln_conv in memo:
        return memo[ln_conv] + time
 
    ln = sorted(ln, reverse = True)
    if ln[0] < 4:
        # print ln, time+ln[0]
        memo[ln_conv] = ln[0]
        return time + ln[0]
    
    options = [time + ln[0]]
    N = ln[0]/2
    for i in range(1, N + 1):
        ln_new = copy.copy(ln)
        ln_new[0] = ln[0] - i
        ln_new.append(i)
        if (ln_new[0] == 0):
            ln_new = ln_new[1:]

        result = solve_sub(ln_new, time + 1)
        options.append(result)
    ret = min(options)
    memo[ln_conv] = ret - time
    return ret

def solve_case(ln):
    print ln
    ln = ln.strip().split(' ')
    ln = [int(x) for x in ln]
    ln = sorted(ln, reverse=True)
    return solve_sub(ln, time = 0)



with open('B-small-attempt2.in') as fin, \
open('B-small-attempt2.out', 'w') as fout:
    case = 0
    NumCases = int(fin.next())
    for case in xrange(1, NumCases+1):
        line = fin.next()
        line = fin.next()
        fout.write("Case #%d: " % case + str(solve_case(line)) + '\n')
        # print line


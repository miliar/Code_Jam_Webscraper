import sys
from itertools import count


def yield_cases(f):
    ''' Generates cases until exhausted. '''
    result = []
    while True:
        line = f.next().strip()
        if len(line):
            result.append(line)
        else:
            yield result
            result = []
    yield result


def judge_case(case):
    ''' Judges a single case.  
    
    Returns a string version of the case, and a list of results.'''
    # horizontal
    results = [judge_string(c) for c in case]

    # vertical
    strungcase = ''.join(case)
    for i in range(4):
        results.append(judge_string(strungcase[i:16:4]))

    # diag
    results.append(judge_string(strungcase[0:16:5]))
    results.append(judge_string(strungcase[3:13:3]))

    return strungcase, results


def judge_string(string):
    ''' Judges a 4 letter string result. '''
    xwin = [i for i in string if i in "XT"]
    owin = [i for i in string if i in "OT"]
    if len(xwin) == 4:
        return 1
    if len(owin) == 4:
        return 0
    else:
        return None


def assess_results(n, case, result):
    ''' Output formatter.  '''
    if 1 in result:
        print 'Case #{}: X won'.format(n)

    elif 0 in result:
        print 'Case #{}: O won'.format(n)

    elif '.' in case:
        print 'Case #{}: Game has not completed'.format(n)

    elif '.' not in case:
        print 'Case #{}: Draw'.format(n)


if __name__ == "__main__":
    filename = 'A-small-attempt0.in'

    c = count(1)
    f = open(filename)
    with f:
        n = int(f.next().strip())
        cases = list(yield_cases(f))
        if len(cases) == n:
            for case in cases:
                strcase, result = judge_case(case)
                print c.next(), strcase, result
                # assess_results(c.next(), strcase, result)

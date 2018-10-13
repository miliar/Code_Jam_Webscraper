import sys
sys.setrecursionlimit(10000000)
def boilerplate(filename):
    with open(filename, 'r') as infi:
        with open('output-'+filename, 'w') as outfi:
            numcases = infi.readline().strip()
            numcases = int(numcases)
            for i in range(numcases):
                case = infi.readline().strip()
                outfi.write(f(i, case)+'\n')

def tester(x):
    return f(0, x)

memoized = {}
def memoize(function):
    global memoized
    def output_function(*args):
        if args in memoized:
            return memoized[args]
        else:
            output = function(*args)
            memoized[args] = output
            return output
    return output_function

def pancakes(casenumber, inp):
    def flip(pancakes, number):
        output = ''
        for i in range(len(pancakes)):
            if i < number:
                output += '+' if pancakes[i] == '-' else '-'
            else:
                output += pancakes[i]
        return output

    @memoize
    def helper(s, k):
        """Minimum number of flips needed"""
        if len(s) <= k:
            if all(cha == '+' for cha in s):
                return 0
            elif len(s) == k and all(cha == '-' for cha in s):
                return 1
            else:
                return float('inf')
        else:
            if s[0] == '-':
                return helper(flip(s[1:], k-1), k) + 1
            else:
                return helper(s[1:], k)

    s, k = inp.split(' ')
    y = helper(s, int(k))
    if y == float('inf'):
        y = 'IMPOSSIBLE'
    return 'Case #%s: %s' % (casenumber + 1, y)


f = pancakes

import sys
from collections import defaultdict
from math import ceil


def quat_mult(a, b): # returns (value, sign)
    if b == '1':
        return (a, 1)
    if a == '1':
        return (b, 1)
    elif a == 'i':
        if b == 'i':
            return ('1', -1)
        elif b == 'j':
            return ('k', 1)
        elif b == 'k':
            return ('j', -1)
        assert False
    elif a == 'j':
        if b == 'j':
            return ('1', -1)
        elif b == 'i':
            return ('k', -1)
        elif b == 'k':
            return ('i', 1)
        assert False
    elif a == 'k':
        if b == 'k':
            return ('1', -1)
        elif b == 'j':
            return ('i', -1)
        elif b == 'i':
            return ('j', 1)
        assert False
    assert False


def mult_init(s):
    global mult_partial_val  # position N == multiplication of the string up to position N-1
    global mult_partial_sign # position N == multiplication of the string up to position N-1
    mult_partial_val = "1"
    mult_partial_sign = [1]
    val = '1'
    sign = 1
    for c in s:
        new_res, new_sign = quat_mult(val, c)
        val = new_res
        sign *= new_sign
        mult_partial_val += val
        mult_partial_sign += [sign]
    #print(mult_partial_val)
    #print(mult_partial_sign)

def quat_inv(a): # returns (value, sign)
    if a == '1':
        return ('1', 1)
    else:
        return (a, -1)

def mult(start, end): # result of multiplying the substring start:end (not including end)
    #print('mult({}, {})'.format(start, end))
    global mult_partial_val
    global mult_partial_sign
    val1 = mult_partial_val[end]
    sign1 = mult_partial_sign[end]
    #print('val1 = {}'.format(val1))
    #print('sign1 = {}'.format(sign1))
    sign2 = mult_partial_sign[start]
    val2, sign3 = quat_inv(mult_partial_val[start])
    val, sign4 = quat_mult(val2, val1)
    sign = sign1 * sign2 * sign3 * sign4
    # print("start = {}, end = {}, val = {}, sign = {}".format(start,end,val,sign))
    return (val, sign)


def solve(fullstring):
    mult_init(fullstring)
    n = len(fullstring)
    for i in range(1, n-1):
        # part1 = fullstring[:i]
        # print('i == {}, part1 == {}'.format(i, part1))
        #print('mult(0, {}) = {}'.format(i, mult(0, i)))
        if mult(0, i) != ('i', 1):
            continue
        for j in range(1, n-i):
            # part2 = fullstring[i:i+j]
            # part3 = fullstring[i+j:]
            # print('j == {}, part2 == {}, part3 == {}'.format(i, part2, part3))
            # assert(part1 + part2 + part3 == fullstring)
            #print('mult({}, {}+{}) = {}'.format(i, i, j, mult(i, i+j)))
            #print('mult({}+{}, {}) = {}'.format(i, j, n, mult(i+j, n)))
            if mult(i, i+j) == ('j', 1) and mult(i+j, n) == ('k', 1):
                return True
    return False

def testcase():
    line = sys.stdin.readline().strip()
    l, x = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    testcase.id += 1
    solution = 'YES' if solve(line * x) else 'NO'
    print('Case #{}: {}'.format(testcase.id, solution))
testcase.id = 0
    
t = int(sys.stdin.readline())
for i in range(t):
    testcase()
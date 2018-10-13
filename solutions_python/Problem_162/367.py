# How to get to the right number of digits, first?

# Have to count to 10.

# What is fastest way to 100?
# 10 -> 19 -> 91 -> 100?

# to 1000?
# 100 -> 109 -> 901 -> 909 -> 990 -> 1000?

# to 10000?
# 1000 -> 1009 -> 9001 -> 9009 -> 9900 -> 9909 -> 9990 -> 9999 -> 10000
#      9        1      8        1       9       1      9        1
       
# Get to correct number of digits.
# Then get each digit, one by one.

# 451
# 1 -> 10 -> 19 -> 91 -> 100 -> 104 -> 401 -> 405 -> 450 -> 451
# 1  9     9     1     9      4     1      4       1     1

# to go from 1 followed by k 0's to 1 followed by (k+1) 0's takes:
# get to (k+1) 9's, then increment

# first nine takes 9 steps
# then swap the nine into position [1 step]
# then next nine takes 8 steps, because of existing one
# then swap [1 step]
# each remaining nine takes 9 steps plus a swap [10 steps]
# then have to increment 9 times [9 steps]
# then increment
# so it's 10*(k+1) - 1?

# 10 -> 100
# 10 -> 19 -> 91 -> 100  :  9 + 1 + 9 = 19
# 100 -> 109 -> 910 -> 919 -> 991 -> 1000  :  9 + 1 + 9 + 1 + 9 = 29
# so 1 to 1000 takes -- 10 + 19 + 29 = 58

# 1 -> 10 [9]
# 10 -> 19 -> 91 -> 100    [9 + 1 + 9 = 19]
# 100 -> 109 -> 901 -> 1000 [9 + 1 + 99 = 109] 
# 1000 -> 1099 -> 9901 -> 10000 [99 + 1 + 99 = 199]
# 10000 -> 10999 -> 99901 -> 100000 [999 + 1 + 99 = [1099]

import sys

def steps_to_n_digits(n):
    if n == 1:
        return 1
    if n == 2:
        return 10
    return steps_to_n_digits(n-1) + 10 ** ((n-1)/2) + 10 ** (n/2) - 1

def val(digits):
    ret = 0
    for d in digits:
        ret = 10*ret + d
    return ret

def not_all_zeros(digits):
    for d in digits:
        if d != 0:
            return True
    return False

def f_steps(digits):
    n = len(digits)
    p0 = steps_to_n_digits(n)

    # just add
    t0 = val(digits) - 10**(n-1)
    ret = t0

    # add + flip + add + flip -- last half of digits can't all be 0
    # t1 = 10 ** 15
    # if not_all_zeros(digits[(n+1)/2:]):
    #     t1 = val(digits[(n+1)/2:])
    #     t1 += 1
    #     t1 += val(reversed(digits[:(n+1)/2])) - 1
    #     t1 += 1
    # ret = min(ret, t1)

    # add + flip + add
    t2 = 10 ** 15
    if not_all_zeros(digits[n/2:]):
        t2 = val(reversed(digits[:n/2]))
        t2 += 1
        t2 += val(digits[n/2:]) - 1
    ret = min(ret, t2)

    # print digits, p0, t0, t2, p0 + ret
    return p0 + ret
    
T = int(sys.stdin.readline())

def rev(x):
    if x % 10 == 0:
        return 1000000
    return val([int(d) for d in reversed(str(x))])

steps = range(1000001)
while True:
    updated = False
    for i in range(10,1000000):
        if steps[i-1] + 1 < steps[i]:
            steps[i] = steps[i-1] + 1

        r = rev(i)
        # if not same_num_digits(r, i):
        #     continue
        if steps[r] + 1 < steps[i]:
            steps[i] = steps[r] + 1
            updated = True
    if not updated:
        break
steps[1000000] = steps[999999] + 1
# print steps[10], steps[100], steps[1000], steps[10000]

for n in range(1, T+1):
    N = [int(d) for d in sys.stdin.readline()[:-1]]

    print "Case #{}: {}".format(n, steps[val(N)])
    # print "Case #{}: {}".format(n, f_steps(N))

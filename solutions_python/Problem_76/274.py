import fileinput

"""
Accepts an array of integers and returns
the maximum sum, or 0 if not possible.
"""
def solve(x):
    return sum(x) - min(x)

"""
Determines if a partition is possible
"""
def possible(x):
    total = 0
    for i in x:
        total = total ^ i
    return not total

"""
Read input and do tests
"""
lines = fileinput.input()
lineno = 0


## Read test cases
T = int(lines[lineno])
lineno += 1

## For each tests
for i in range(T):
    x = []
    N = int(lines[lineno])
    lineno += 1
    nums = lines[lineno].split(' ')
    for j in nums: 
        x.append(int(j))
    if possible(x):
        ans = solve(x)
    else: ans = 'NO'
    print 'Case #%(case)d: %(ans)s' % {'case': i+1, 'ans': ans}
    lineno+=1



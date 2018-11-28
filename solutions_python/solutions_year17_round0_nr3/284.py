"""
Google Code Jam 2017
Qualification Round
Problem C

Author  : chaotic_iak
Language: Python 3.5.2
"""

################################################### SOLUTION

def initialize_solver():
    pass

def solve(left, len1, n1, n2):
    spaces = [n1, n2]
    if len1 % 2:
        spaces = spaces + [0]
    else:
        spaces = [0] + spaces
        len1 -= 1
    lenend = len1 // 2
    result = [0, 0]

    for i in range(2,-1,-1):
        if left <= spaces[i]:
            return len1+i-1
        left -= spaces[i]
        result[i//2] += spaces[i]
        result[(i+1)//2] += spaces[i]
    return solve(left, lenend, result[0], result[1])

def solve_testcase():
    n,k = read()
    res = solve(k, n, 1, 0)
    return [(res+1)//2, res//2]

#################################################### HELPERS

def read(callback=int, split=True):
    if sfile:
        input_line = sfile.readline().strip()
    else:
        input_line = input().strip()
    if split:
        return list(map(callback, input_line.split()))
    else:
        return callback(input_line)

def write(value="\n"):
    if value is None: return
    try:
        if not isinstance(value, str):
            value = " ".join(map(str, value))
    except:
        pass
    if tfile:
        tfile.write(value)
    else:
        print(value, end="")

# None: Single testcase, solve_testcase() only
# str : Multiple testcase, print output_format before
#                          %d replaced with case number
output_format = "Case #%d: "

filename = input().strip()
sfile = None
tfile = None
if filename != "":
    sfile = open(filename + ".in", "r")
    sfile.seek(0)
    tfile = open(filename + ".out", "w")

if output_format == None:
    solve_testcase()
else:
    initialize_solver()
    total_cases, = read()
    for case_number in range(1, total_cases+1):
        write(output_format.replace("%d", str(case_number)))
        write(solve_testcase())
        write()
if tfile is not None: tfile.close()

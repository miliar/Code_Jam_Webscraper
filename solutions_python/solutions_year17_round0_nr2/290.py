"""
Google Code Jam 2017
Qualification Round
Problem B

Author  : chaotic_iak
Language: Python 3.5.2
"""

################################################### SOLUTION

def initialize_solver():
    pass

def solve(d, a):
    if a == []:
        return [d]
    check = solve(a[0], a[1:])
    if d > check[0]:
        return [d-1] + [9]*len(a)
    return [d] + check

def solve_testcase():
    n = read(callback=str, split=False)
    a = list(map(int, n))
    return str(int("".join(map(str, solve(a[0], a[1:])))))

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

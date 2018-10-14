import sys
import operator

def read_problem(line):
    nums = map(int, line.split())
    return nums

def solve(nums):
    check = reduce(operator.xor, nums)
    if check != 0:
        return 'NO'
    nums.sort()
    sumed = sum(nums[1:])
    return sumed



if (len(sys.argv) == 2):
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[1]+'.out.txt', 'w')
else:
    infile = sys.stdin
    outfile = sys.stderr

input_iter = iter(infile)
T=(int(next(input_iter)))
for i in xrange(T):
    N = next(input_iter)
    problem = read_problem(next(input_iter))
    s = solve(problem)
    print >>outfile, "Case #%i: %s" % (i+1,s)

infile.close()
outfile.close()

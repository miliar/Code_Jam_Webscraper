from sys import argv
from re import sub
from math import factorial

def count_recyclable_pairs(num,A,B,digits):
    """Counts the number of distinct numbers that can be obtained from
    "recycling" first, then uses permutations to determine the number
    of such pairs. Then, the distinct numbers are added to the set of
    numbers that have already been counted to avoid double-counting
    and reduce processing time."""
    global counted
    dist_nums = set()
    num = str(num)
    for _ in range(digits):
        int_form = int(num)
        if A <= int_form <= B:
            dist_nums.add(int_form)
            num = num[1:]+num[0]  # rotates 1 to the left
        else:
            num = num[1:]+num[0]
            continue  # not in range, starts with 0
    # nums with no pairs aren't problematic because choose2(1) = 0
    # but no need to add to counted because no pairs to save processing time
    if len(dist_nums) > 1:
        counted.update(dist_nums)
    return choose2(len(dist_nums))
    
def choose2(n):
    if n < 2:
        return 0
    return factorial(n)//(factorial(n-2)*2)

def read(inputfile):
    g = inputfile.readline()
    return sub('\n','',g)

inp = open(argv[1])
T = int(read(inp))

for t in range(T):
    A, B = list(map(int,read(inp).split()))
    counted = set()  # counted is set of NUMBERS (not pairs) that have been counted
    paircount = 0
    digits = len(str(A))
    for num in range(A,B+1):
        if num in counted:
            continue
        else:
            paircount += count_recyclable_pairs(num,A,B,digits)
    print("Case #%s:" % (t+1), paircount)

import sys
from sets import Set


def read_arr(f):
    rows = []
    for i in xrange(0,4):
        rows.append(f.readline().strip().split())

    return rows

def solve(ans1, arr1, ans2, arr2):
    a1 = Set(arr1[ans1-1])
    a2 = Set(arr2[ans2-1])
    res = a1.intersection(a2)
    if len(res) < 1:
        return "Volunteer cheated!"
    elif len(res) > 1:
        return "Bad magician!"
    else:
        return res.pop()


if len(sys.argv) > 1:
    filename = sys.argv[len(sys.argv)-1]
else:
    raise Exception("Missing file paramenter")


f = open(filename, 'r')
n = int(f.readline().strip())

for line_no in xrange(0, n):
    ans1 = int(f.readline().strip())
    arr1 = read_arr(f)
    ans2 = int(f.readline().strip())
    arr2 = read_arr(f)
    ans = solve(ans1, arr1, ans2, arr2)
    case = line_no + 1
    print "Case #{}: {}".format(case, ans)

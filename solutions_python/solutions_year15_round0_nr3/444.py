import sys
import re

class Teed(object):
    """Wraps a file object. It behaves mostly like the original one,
     but the calls to "write" are replicated to stdout.

     The writelines method is not overriden yet.
     """

    def __init__(self, original):
        self._orig = original

    def write(self, str):
        sys.stdout.write(str)
        self._orig.write(str)

    def __getattr__(self, property):
        """Delagate all other properties
           and method calls to wrapped object"""
        return self._orig.__getattribute__(property)

def main():
    name = re.match(r"^(.*\.)in$", sys.argv[1]).group(1) + "out"

    with open(sys.argv[1]) as f:
        orig_out = sys.stdout
        with open(name, "w") as out_f:
            wrapped = Teed(out_f)
            parse(f, wrapped)

def parse(inp, out):
    cases = int(inp.next().strip())
    for i in range(cases):
        c = parse_case(inp)
        print "Solving case #%d (%s)" % (i + 1, c)
        solution = solve(c)
        print >> out, "Case #%d: %s" % (i + 1, solution)

from itertools import imap, groupby, repeat
from functools import reduce
import operator

def parse_case(inp):
    l, x = map(int, inp.next().split())
    s = inp.next().strip()
    assert l == len(s)
    return x, s

def solve((l, x)):
    if bruteforce(l, x) is True:
        return "YES"
    else:
        return "NO"

def qmul(q1, q2):
    return (
        q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3],
        q1[0]*q2[1] + q1[1]*q2[0] + q1[2]*q2[3] - q1[3]*q2[2],
        q1[0]*q2[2] - q1[1]*q2[3] + q1[2]*q2[0] + q1[3]*q2[1],
        q1[0]*q2[3] + q1[1]*q2[2] - q1[2]*q2[1] + q1[3]*q2[0],
    )

quat_to_name = {
        ( 1,  0,  0,  0): "1",
        (-1,  0,  0,  0): "-1",
        ( 0,  1,  0,  0): "i",
        ( 0, -1,  0,  0): "-i",
        ( 0,  0,  1,  0): "j",
        ( 0,  0, -1,  0): "-j",
        ( 0,  0,  0,  1): "k",
        ( 0,  0,  0, -1): "-k",
}

quats = set(quat_to_name.keys())

name_to_quat = { name: h for h, name in quat_to_name.items() if len(name) == 1 }

def bruteforce(l, x):
    size = l * len(x)
    lx = len(x)
    nums = map(lambda l: name_to_quat[l], x)
    def getn(n):
        return nums[n % lx]

    def getns(start, end):
        for i in range(start, end):
            yield getn(i)

    wanted = name_to_quat["i"], name_to_quat["j"], name_to_quat["k"]

    first = getn(0)
    first_pos = 0

    for i in range(1, size):
        if first == name_to_quat["i"]:
            break
        first_pos = i
        first = qmul(first, getn(i))
    else:
        return 1

    last = getn(size - 1)
    last_pos = size - 1

    for i in reversed(range(first_pos + 1, size - 1)):
        # print i, quat_to_name[getn(i)], quat_to_name[last]
        if last == name_to_quat["k"]:
            break
        last_pos = i
        last = qmul(getn(i), last)
    else:
        return 2

    if last_pos < first_pos + 2:
        return 4

    if quat_to_name.get(reduce(qmul, getns(first_pos + 1, last_pos))) != "j":
        return 3

    return True


    for j in range(i + 2, len(nums)):
        # print i, j, s[0:i+1], "|", s[i+1:j], "|", s[j:]
        second = reduce(qmul, nums[i+1:j])
        third = qmul(nums[j], third)

        # print map(quat_to_name.get, (first, second, third))
        if (firsts[i], second, third) == wanted:
            return True

    return False

if __name__ == "__main__":
    main()

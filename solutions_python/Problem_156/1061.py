import sys

f = sys.stdin #open('C-small-practice.in')
def get_int(): return int(f.readline())
def get_ints(): return [int(s) for s in f.readline().split()]

for t in range(get_int()):
    n = get_int()
    a = get_ints()
    res = min(
        eat + sum((x+eat-1) // eat - 1 for x in a)
        for eat in range(1, max(a) + 1))
    print("Case #{}: {}".format(t+1, res))

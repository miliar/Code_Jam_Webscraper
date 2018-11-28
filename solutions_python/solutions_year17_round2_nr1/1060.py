
def do_work(other_horses, d):
    max_time = max((d-ki)/si for ki, si in other_horses)
    return d/max_time





t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    d, n = input().split()
    d, n = int(d), int(n)
    other_horses = []
    for j in range(n):
        ki, si = input().split()
        other_horses.append((int(ki), int(si)))
    result = do_work(other_horses, d)
    print("Case #{}: {}".format(i, result))

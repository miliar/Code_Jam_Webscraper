import math

def pancake_side(p2):
    return 2 * math.pi * p2[0] * p2[1]

def comb_and_comp(lst, n):
    # no combinations
    if len(lst) < n:
        return
    # trivial 'empty' combination
    if n == 0 or lst == []:
        yield [], lst
    else:
        first, rest = lst[0], lst[1:]
        # combinations that contain the first element
        for in_, out in comb_and_comp(rest, n - 1):
            yield [first] + in_, out
        # combinations that do not contain the first element
        for in_, out in comb_and_comp(rest, n):
            yield in_, [first] + out


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(x) for  x in  input().split(" ")]  # read a list of integers, 2 in this case
    p = []
    for i2 in range(0, n):
        r, h = [int(x) for x in  input().split(" ")]  # read a list of integers, 2 in this case
        p.append((r, h))

    p.sort(reverse=True)
    #print("n: {}   k: {}".format(n, k))
    #kkprint(p)

    max_area = 0
    for base_pancake in range(0, n):
        #print("Base radius {}".format(p[base_pancake][0]))
        area = p[base_pancake][0]**2*math.pi
        area += pancake_side(p[base_pancake])
        next_pancakes = p[base_pancake + 1:]
        if len(next_pancakes) < k - 1: continue
        #kj,sprint(next_pancakes)
        next_pancakes.sort(reverse=True, key=lambda x: x[0] * x[1])
        #print(next_pancakes)
        for l in range(0, k - 1):
            area += pancake_side(next_pancakes[l])

        #print("Area {}\n".format(area))
        max_area = max(max_area, area)

    #max_area2 = 0
    #for x2 in comb_and_comp(p, k):
    #    x = x2[0]
    #    area = x[0][0] ** 2 * math.pi
    #    for p2 in x:
    #        area += pancake_side(p2)
    #    max_area2 = max(max_area2, area)
    #    print(x)
    #    print(max_area)
    #    print(max_area2)
    #    assert(max_area + 10 >= max_area2)
#
    #print(max_area)
    #print(max_area2)

    print("Case #{}: {}".format(i, max_area))
    #print("#################################")

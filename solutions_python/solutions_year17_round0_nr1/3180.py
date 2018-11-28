

def flip(stove, pos, size):
    res = []

    for i, val in enumerate(stove):
        if i >= pos and i < pos + size:
            if val == "+":
                res.append("-")
            else:
                res.append("+")
        else:
            res.append(val)

    return "".join(res)


def flipit(start, size, goal_stove):
    q = [(start, 0)]
    seen = set()
    seen.add(start)

    while len(q) != 0:
        stove, d = q.pop(0)

        if stove == goal_stove:
            return d

        for i in range(len(stove) - size + 1):
            possible = flip(stove, i, size)

            if possible not in seen:
                seen.add(possible)
                q.append((possible, d+1))

    return "IMPOSSIBLE"



t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    stove, size = input().split(" ")  # read a list of integers, 2 in this case

    goal = "+" * len(stove)

    res = flipit(stove, int(size), goal) 

    print("Case #{}: {}".format(i, res))




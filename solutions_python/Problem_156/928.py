from queue import PriorityQueue

def eat(l):
    i = 0
    while i < len(l):
        l[i] -= 1
        if l[i] <= 0:
            l[i] = 0
        i += 1
    while len(l) > 1 and l[-1] == 0:
        l = l[:-1]
    return tuple(l)

def lift(l):
    res = []
    need_zero = True
    i = l.index(max(l))
    diners_plate = l[i]
    for nb_pancakes in range(1, diners_plate + 1):
        for k in range(len(l)):
            if i != k:
                if l[k] == 0:
                    need_zero = False
                l[i] -= nb_pancakes
                l[k] += nb_pancakes
                res.append(tuple(l))
                l[k] -= nb_pancakes
                l[i] += nb_pancakes
        if need_zero:
            l[i] -= nb_pancakes
            l.append(nb_pancakes)
            res.append(tuple(l))
            del l[len(l) - 1]
            l[i] += nb_pancakes
    for i in range(len(res)):
        if res[i][-1] == 0:
            res[i] = res[i][:-1]
    return res

def next_states(s):
    l = list(s)
    return lift(l) + [eat(l)]

def h(diners):
    n = len([i for i in diners if i != 0])
    if n == 0:
        return 0
    else:
        return sum(diners) / n

def isgoal(x):
    return len(x) == 0 or x[0] == 0 and isgoal(x[1:])

def astar(tab):
    cost = {tab : 0}
    frontier = PriorityQueue()
    frontier.put((h(tab), tab))
    while not frontier.empty():
        _, x = frontier.get()
        if isgoal(x):
            return cost[x]
        for y in next_states(x):
            newcost = cost[x] + 1
            if y not in cost or newcost < cost[y]:
                cost[y] = newcost
                frontier.put((newcost + h(y), y))
    print("Something went wrong...")

with open("B-small-attempt5.in") as f:
    n = int(f.readline())
    for i in range(n):
        D = int(f.readline())
        tab = tuple([int(x) for x in f.readline().split(' ')])
        res = astar(tab)
        print("Case #%d:" % (i + 1), res)

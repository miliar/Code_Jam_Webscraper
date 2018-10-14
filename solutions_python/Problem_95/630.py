#!/usr/bin/python2

import sys

'''
class Auxiliar:
    def __init__(self):
        self.a = 0
        self.b = 0

    def func(self):
        self.a = b

c = Auxliar()
'''

def func():
    for path in recursives:
        len_path = len(path)
        if paths[1]:
            if len(paths[1][0]) < len_path:
                break
        for other in neigh[path[-1]]:
            if paths[other]:
                len_path_other = len(paths[other][0])
                if len_path > len_path_other:
                    continue
                elif len_path == len_path_other:
                    paths[other].append(path)
                    recursives.append(path + [other])
                else:
                    print path
                    print paths[other][0]
                    import ipdb; ipdb.set_trace()
                    raise Exception("NOOOOOOOOOO PETAO")
            else:
                paths[other] = [path]
                recursives.append(path + [other])

def calc_neigh(x):
    n = set()
    for hole in holes:
        if hole[0] == x:
            n.add(hole[1])
        elif hole[1] == x:
            n.add(hole[0])

    return n

with open(sys.argv[1]) as f:
    lines = f.readlines();

# Quito primera linea que suele ser el numero de casos que hay
# y se puede deducir del numero de lineas del fichero restantes
lines = lines[1:]

n_case = 0
while lines:
    n_case += 1
    # import ipdb; ipdb.set_trace()
    # Ejemplo leo una linea que viene el numero de coches y aviones
    # posteriores
    P, W = [int(x) for x in lines.pop(0).split()]

    holes = [x for x in lines.pop(0).split()]
    holes = [x.split(',') for x in holes]
    worm_holes = []
    for hole in holes:
        worm_holes.append([int(hole[0]),int(hole[1])])

    holes = worm_holes

    paths = dict()
    neigh = dict()


    for x in range(P):
        paths[x] = []
        neigh[x] = calc_neigh(x) 

    paths[0] = [[0]]

    recursives = [[0]]

    func()

    max_t = 0

    for good in paths[1]:
        total = set()
        for planet in good:
            total = total.union(neigh[planet])

        total = total - set(good)
        max_t = max(max_t, len(total))

    print "Case #%d: %d %d" % (n_case, len(paths[1][0]) - 1, max_t)

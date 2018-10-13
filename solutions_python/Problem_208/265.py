# coding: utf8
# Copyright: MathDecision

def leq(x, y):
    return (x[0] >= y[0]) and (x[1] <= y[1]) and (x[2] <= y[2])

def maximal(lst):
    maxs = []
    for x in lst:
        less = False
        great = False
        appgreat = []
        for i, m in enumerate(maxs):
            if leq(x, m):
                less = True
                break
            elif leq(m, x):
                great = True
                appgreat.append(i)
        if great:
            for i in reversed(appgreat):
                del maxs[i]
        if not less:
            maxs.append(x)
    return maxs



def solutionsmall(cities, D):
    e, s = cities[0]
    info = [(0, e, s)]
    for i in range(1, len(cities)):
        # print '*********'
        # print i
        # print info
        newdist = D[i - 1][i]
        info = [(t + 1.0 * newdist / ss, ee - newdist, ss) for t, ee, ss in info if ee - newdist >= 0]
        if i == len(cities) - 1:
            return min(t for t, ee, ss in info if ee >= 0)
        # print info
        e, s = cities[i]
        info += [(t, e, s) for t, ee, ss in info]
        # print info
        info = [(t, ee, ss) for t, ee, ss in info if ee > 0]
        info = maximal(info)
        # print info
    return min([t for t, ee, ss in info])

if __name__ == '__main__':
    #
    # print maximal([(0, 1, 1), (1, 2, 2), (1, 4, 4), (0, 1, 2)])
    # exit()

    file_number = 1
    problem_name = 'ponyexpress'
    infile = '{}{}.in'.format(problem_name, file_number)
    outfile = '{}{}.out'.format(problem_name, file_number)
    responses = []
    with open(infile, 'r') as f:
        cases = int(f.readline())
        for _ in range(cases):
            # print '----------------'
            N, Q = map(lambda x: int(x), f.readline().split(' '))
            cities = []
            for i in range(N):
                E, S = map(lambda x: float(x), f.readline().split(' '))
                cities.append((E, S))
            adjacency = []
            for i in range(N):
                adjacency.append(map(lambda x: float(x), f.readline().split(' ')))
            routes = []
            for i in range(Q):
                U, V = map(lambda x: float(x), f.readline().split(' '))
                routes.append([U, V])
            # print cities
            # print adjacency
            # print routes
            res = solutionsmall(cities, adjacency)
            responses.append(res)

    with open(outfile, 'w') as f:
        for i, r in enumerate(responses):
            f.write('Case #{}: {}\n'.format(i + 1, r))

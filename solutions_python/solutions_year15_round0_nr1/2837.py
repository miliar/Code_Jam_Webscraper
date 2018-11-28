import sys

def n_req(dist):
    return max((0, max(dist) - len(list(filter(lambda x: x < max(dist), dist)))))

def gen_dist(l):
    dist = []
    for i, n in enumerate(l):
        dist.extend([i for _ in range(n)])
    return dist


tests = (([1,1,1,1,1], 0),
         ([0,9], 1),
         ([1,1,0,0,1,1], 2),
         ([1], 0)
         )

def count(dist):
    dist = sorted(dist)
    n = 0
    extras = 0
    for p in dist:
        if p > n:
            extras += p - n
            n += p - n
        n += 1
    return extras


def new():
    for test in tests:
        dist = gen_dist(test[0])
        #print(dist, count(dist), test[1])
        assert count(gen_dist(test[0])) == test[1]


    data = sys.stdin.read().split("\n")[1:]
    for i, line in enumerate(data):
        if line:
            line_data = [int(c) for c in line.split()[1]]
            print("Case #" + str(i+1) + ": " + str(count(gen_dist(line_data))))

new()

def old():
    for test in tests:
        d = gen_dist(test[0])
        n = n_req(d)
        #print(d, n_req(d), test[1])
        assert n == test[1]

    data = sys.stdin.read().split("\n")[1:]
    for i, line in enumerate(data):
        if line:
            line_data = [int(c) for c in line.split()[1]]
            print("Case #" + str(i+1) + ": " + str(n_req(gen_dist(line_data))))


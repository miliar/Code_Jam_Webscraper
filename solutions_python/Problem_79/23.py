import sys

def get_line():
    return sys.stdin.readline().strip()

def read_nums():
    return [int(item) for item in get_line().split(" ")]

def get_match(word, char):
    res = []
    for i in xrange(len(word)):
        if word[i] == char:
            res.append(i)
    return tuple(res)

def solve(groups, order):
    points = []
    for group in groups:
        points.append( (0, group) )

    results = []
    for char in order:
        if len(points) <= 0:
            break
        new_points = []
        for point in points:
            do_try = False
            if len(point[1]) <= 1:
                results.append( (point[0], point[1][0] ) )
                continue
            new_group = {}
            for word in point[1]:
                match = get_match(word, char)
                if len(match) > 0:
                    do_try = True
                if match not in new_group:
                    new_group[match] = []
                new_group[match].append(word)
            for (match, group) in new_group.items():
                if do_try and len(match) == 0:
                    new_points.append( (point[0]-1, group) )
                else:
                    new_points.append( (point[0], group) )
        points = new_points
    results.sort()
    score = results[0][0]
    tmp = []
    for result in results:
        if result[0] != score:
            break
        tmp.append( result[1] )
    return tmp

(T,) = read_nums()
for test in range(1, T+1):
    (N, M) = read_nums();
    groups = {}
    words = []
    for i in range(N):
        word = get_line()
        words.append(word)
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    groups = groups.values()

    results = []
    for i in range(M):
        order = get_line()
        tmp = set(solve(groups, order))
        flag = False
        for word in words:
            if word in tmp:
                results.append( word )
                flag = True
                break
        if not flag:
            print "Not Found!"
    print "Case #%d: %s" % (test, " ".join(results))


import sys
import math

def check_train(chars, last_char, part):
    used_chars = set(chars)
    for c in part:
        if c in used_chars and c != last_char:
            return False
        used_chars.add(c)
        last_char = c

    return True

def generate_config(N, pos, trains, used, last_part, chars):
    if N == pos: # valid config, add 1
        return 1
    sum = 0
    # add last part first
    used_chars = chars.copy()
    for c in last_part:
        used_chars.add(c)
    # check other parts
    for i in xrange(N):
        if not used[i] and check_train(used_chars, last_part[-1], trains[i]):
            used[i] = True
            sum += generate_config(N, pos + 1, trains, used, trains[i], used_chars)
            used[i] = False # turn off usage, it has been checked
    return sum

def get_solution_bf(trains): # brute force
    N = len(trains)
    used = [False] * N
    return generate_config(N, 0, trains, used, ' ', set([]))

def linked(t1, t2):
    for c in t1:
        if t2.find(c) >= 0:
            return True
    return False

def get_components(trains):
    N = len(trains)
    links = [[] for i in xrange(N)] # neighbour lists
    for t1 in xrange(N - 1):
        for t2 in xrange(t1 + 1, N):
            if linked(trains[t1], trains[t2]):
                links[t1].append(t2)
                links[t2].append(t1)

    # get different component groups using depth first search
    used = N * [False]
    def dfs(node, group):
        # add node to this group, mark used
        used[node] = True
        group.append(trains[node])

        for n in links[node]:
            if not used[n]:
                dfs(n, group)

    groups = []
    for i in xrange(N):
        if not used[i]:
            group = []
            dfs(i, group)
            groups.append(group)

    return groups

def same_char(train):
    if len(train) == 1:
        return True
    for i in xrange(1, len(train)):
        if train[i - 1] != train[i]:
            return False
    return True

def get_group_count(g):
    chars = {}
    for i in xrange(len(g) - 1, -1, -1):
        if same_char(g[i]):
            c = g[i][0]
            g.pop(i)

            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    res = 1

    for c, count in chars.iteritems():
        g.append(c) # one kepviselo
        res *= math.factorial(count)

    res *= get_solution_bf(g)
    return res

def get_solution(trains):
    N = len(trains)
    P = 1000000007
    groups = get_components(trains)
    result = math.factorial(len(groups)) % P
    for g in groups:
        c = get_group_count(g)
        result = (result * c) % P
    return result

if __name__ == "__main__":
    f = sys.stdin
    T = int(f.readline())
    for i in xrange(T):
        N = int(f.readline())
        trains = f.readline().strip().split()
        configs = get_solution(trains)

        print "Case #%d: %d" % (i + 1, configs)
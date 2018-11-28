#!/usr/bin/pypy

def read_line():
    s = raw_input()
    while s == "":
        s = raw_input()
    return s

def read_str():
    return read_line().strip()

def read_int():
    return int(read_line())

def read_ints():
    return tuple(int(s) for s in read_line().split())

def get_indices(M, N):
    if M == 0:
        yield ()
        return
    for vals in get_indices(M - 1, N):
        for i in range(N):
            yield vals + (i,)

def get_total_nodes(S, i_assignments):
    N = len(i_assignments)
    trie_nodes = tuple(set() for i in range(N))
    for s, i in zip(S, i_assignments):
        trie = trie_nodes[i]
        for j in range(0, len(s) + 1):
            trie.add(s[:j])
    return sum(len(trie) for trie in trie_nodes)

def solve():
    M, N = read_ints()
    S = tuple(read_str() for i in range(M))

    ways = 0
    most = 0
    for i_assignments in get_indices(M, N):
        total_nodes = get_total_nodes(S, i_assignments)
        if total_nodes < most:
            continue
        if total_nodes > most:
            most = total_nodes
            ways = 0
        # print(most, trie_nodes)
        ways += 1
    return "{0} {1}".format(most, ways % 1000000007)

if __name__ == "__main__":
    T = int(read_line())
    for i in range(1, T+1):
        solution = solve()
        print "Case #{0}: {1}".format(i, solution)

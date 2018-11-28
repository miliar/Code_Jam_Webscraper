import sys
import networkx as nx
sys.stdout = open('c_big.out', 'w')
sys.stdin  = open("c_big.in", 'r')
sys.setrecursionlimit(1500)




def solve():
    N, Q = map(int, raw_input().split())
    horses = {}
    for i in range(1, N + 1):
        horses[i] = map(int, raw_input().split())
        # horse is (max dist, speed)

    G = nx.DiGraph()
    for i in range(1, N + 1):

        dist = map(int, raw_input().split())
        for j in range(1, N + 1):
            if dist[j - 1] != -1:
                G.add_edge(i, j, weight=dist[j-1])


    fastest_horse = {}
    length = nx.all_pairs_dijkstra_path_length(G)
    #print length
    #print "poop"
    for i in range(1, N + 1):
        fastest_horse[i] = {}
        for j in range(1, N + 1):
            if i not in length:
                fastest_horse[i][j] = float('inf')
                continue
            if j not in length[i]:
                fastest_horse[i][j] = float('inf')
                continue
            shortest_length = length[i][j]
            if shortest_length > horses[i][0]:
                fastest_horse[i][j] = float('inf')
            else:
                fastest_horse[i][j] = shortest_length / float(horses[i][1])


    sp = {}
    for i in range(1, N + 1):
        sp[i] = {}
        for j in range(1, N + 1):
            sp[i][j] = fastest_horse[i][j]

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if sp[i][j] > sp[i][k] + sp[k][j]:
                    sp[i][j] = sp[i][k] + sp[k][j]
    ans = []
    for _ in range(Q):
        u, v = map(int, raw_input().split())
        ans.append(sp[u][v])
    return " ".join(map(str, ans))

    shortest_from = {}
    # shortest_from[i][j] = shortest time from i to j, using horse j
    #print fastest_horse


T = int(raw_input())
for i in range(1, T + 1):
    ans = solve()
    print "Case #" + str(i) + ": " + str(ans)
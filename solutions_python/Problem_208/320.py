import sys
from decimal import *

def find_nonzero(row):
    for idx, elem in enumerate(row):
        if elem != -1:
            return idx
    return None 

def solve(horses, route_matrix, queries):
    node_order = []
    visited = set()
    for idx, row in enumerate(route_matrix):
        temp_ix = idx
        current_ordering = []
        while temp_ix is not None and temp_ix not in visited:
            visited.add(temp_ix)
            current_ordering.append(temp_ix)
            temp_ix = find_nonzero(route_matrix[temp_ix])
        if current_ordering:
            if not node_order or temp_ix == node_order[0]:
                node_order = current_ordering + node_order
            else:
                node_order = node_order + current_ordering
            current_ordering = []

    dp = [[-1 for ele in range(len(node_order))] for elex in range(len(node_order))]
    for i in range(len(node_order)):
        cumulative_dist = 0
        dist, speed = horses[node_order[i]]
        for j in range(i+1, len(node_order)):
            cumulative_dist += route_matrix[node_order[j-1]][node_order[j]]
            if cumulative_dist > dist:
                break
            else:
                dp[i][j] = Decimal(cumulative_dist) / Decimal(speed)

    for col in range(len(node_order)):
        for row in range(col, -1, -1):
            if row != col and col != row - 1:
                min_candidate = dp[row][col]
                t_row = col - 1
                t_col = col - 1
                while t_row != row:
                    s = dp[t_row][col] + dp[row][t_col]
                    if min_candidate == -1 or s < min_candidate:
                        min_candidate = s
                    t_col = t_col - 1
                    t_row = t_row - 1
                dp[row][col] = min_candidate
 
    results = []
    for query in queries:
        results.append(dp[query[0]-1][query[1]-1])
    return " ".join(map(lambda x: "{:.6f}".format(x), results))

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for case in range(T):
        N, Q = map(int, sys.stdin.readline().split())
        horses = []
        for x in range(N):
            total_dist, speed = map(int, sys.stdin.readline().split())
            horses.append((total_dist, speed))
        route_matrix = []
        for x in range(N):
            route_row = map(int, sys.stdin.readline().split())
            route_matrix.append(route_row)
        queries = []
        for x in range(Q):
            origin, destination = map(int, sys.stdin.readline().split())
            queries.append((origin, destination))
        print "Case #{}: {}".format(case + 1, solve(horses, route_matrix, queries))

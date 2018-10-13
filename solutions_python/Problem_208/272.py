from functools import lru_cache

T = int(input())
INF = 10 ** 12 + 47

def solve_query_small(u, v, horses, distances):
    N = len(horses)

    @lru_cache(maxsize=None)
    def traverse(rem_distance, speed, curr_town, target_town):
        # If we are in target_town, we reached the destination
        if curr_town == target_town:
            return 0

        # We are in curr_town, find all towns, we can travel to:

        for town in range(N):
            distance = distances[curr_town][town]
            if distance == -1:
                continue
            if distance <= rem_distance:
                # Our horse is enough to go here!
                # We can switch or not switch
                new_distance, new_speed = horses[town]
                return min(
                    traverse(rem_distance - distance, speed, town, target_town),
                    traverse(new_distance, new_speed, town, target_town)
                ) + (distance / speed)
        return INF

    # We start in town U
    max_distance, speed = horses[u]
    return traverse(max_distance, speed, u, v)


def solve_case():
    n, q = [int(x) for x in input().split()]
    horses = [[]] + [[int(x) for x in input().split()] for i in range(n)]
    distances = [[]] + [[-1] + [int(x) for x in input().split()] for i in range(n)]
    queries = [[int(x) for x in input().split()] for i in range(q)]
    for u, v in queries:
        print(' {}'.format(solve_query_small(u, v, horses, distances)), end='')


for I in range(1, T + 1):
    print("Case #{}:".format(I), end='')
    solve_case()
    print()

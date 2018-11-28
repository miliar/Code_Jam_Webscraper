import sys
sys.stdout = open('b.out', 'w')
sys.stdin  = open("b.in", 'r')
sys.setrecursionlimit(1500)
T = int(raw_input())


def good(S):
    for c in S:
        if c == '-':
            return False
    return True

def algorithm(S, K):
    pass

def solve():
    N, P = map(int, raw_input().split())
    ingredients = []
    required = map(int, raw_input().split())
    assert len(required) == N
    for _ in range(N):
        ingredients.append(sorted(map(int, raw_input().split())))
        assert len(ingredients[-1]) == P


    count_per_kit = 1

    total_kits = 0
    curr_indices = [0] * N
    #print curr_indices
    #print ingredients
    while True:
        can_kit = True
        for i in range(N):
            #print N, i, curr_indices[i]
            while ingredients[i][curr_indices[i]] < 0.9 * required[i] * count_per_kit:
                curr_indices[i] += 1
                if curr_indices[i] == P:
                    return total_kits
            if ingredients[i][curr_indices[i]] > 1.1 * required[i] * count_per_kit:
                count_per_kit += 1
                can_kit = False
        if can_kit:
            total_kits += 1
            for i in range(N):
                curr_indices[i] += 1
                if curr_indices[i] == P:
                    return total_kits




for i in range(1, T + 1):
    ans = solve()
    print "Case #" + str(i) + ": " + str(ans)
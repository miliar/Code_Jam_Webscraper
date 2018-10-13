
def run_test():
    N, P = map(int, input().split())
    recipe = [int(x) for x in input().split()]
    assert len(recipe) == N
    packages = [[int(x) for x in input().split()]
                for i in range(N)]
    assert all(len(line) == P for line in packages)
    for i in range(N):
        packages[i].sort()
        for j in range(P):
            packages[i][j] *= 10
    indices = [0 for i in range(N)]
    total_packages = 0
    recipe_low = [ing * 9 for ing in recipe]
    recipe_high = [ing * 11 for ing in recipe]
    cur_recipe_low = recipe_low[:]
    cur_recipe_high = recipe_high[:]
    while all(ind < P for ind in indices):
        for i in range(N):
            while (indices[i] < P and
                   packages[i][indices[i]] < cur_recipe_low[i]):
                indices[i] += 1

        while (all(ind < P for ind in indices) and
               all(packages[i][ind] <= cur_recipe_high[i]
                   for i, ind in enumerate(indices))):
            total_packages += 1
            for i in range(N):
                indices[i] += 1

        for i in range(N):
            cur_recipe_low[i] += recipe_low[i]
            cur_recipe_high[i] += recipe_high[i]
    return total_packages

for i in range(1, int(input()) + 1):
    print("Case #{}: {}".format(i, run_test()))

# Google Code Jam 2017
# Round 1A
# Problem B. Ratatouille

import numpy as np

t = int(input())  # read a line with a single integer
for case in range(1, t + 1):
    N, P = map(int, input().split())
    recipe = np.array([int(c) for c in input().split()])
    assert len(recipe) == N
    packages = np.zeros((N,P), dtype=int)
    for i in range(N):
        packages[i] = [int(c) for c in input().split()]
    packages = np.sort(packages, axis=1)

    min_servings = np.ceil(packages/(recipe[...,None]*1.1)).astype(int)
    max_servings = np.floor(packages/(recipe[...,None]*0.9)).astype(int)
    valid = min_servings <= max_servings
    kits = 0

    if valid.any():
        for num_servings in range(np.min(min_servings), np.max(max_servings) + 1):
            how_many = np.min(np.logical_and(np.logical_and(min_servings <= num_servings, max_servings >= num_servings), valid).sum(1))
            if how_many > 0:
                for i in range(how_many):
                    z = np.logical_and(np.logical_and(min_servings <= num_servings, max_servings >= num_servings), valid)
                    for j in range(N):
                        valid[j,np.argmax(z[j] > 0)] = False
                    kits += 1
            if not valid.any():
                break
   
    print("Case #{0}: {1}".format(case, kits))

# --- HOW TO USE ---
# python test.py < input > output

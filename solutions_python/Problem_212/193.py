num_cases = int(input())

groups = {
    2: [[1, 0], [0, 2]],
    3: [[1, 0, 0], [0, 1, 1], [0, 3, 0], [0, 0, 3]],
    4: [[1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 2, 0], [0, 2, 1, 0], [0, 0, 1, 2], [0, 4, 0, 0], [0, 0, 0, 4]]
}

for c in range(num_cases):
    N, P = map(int, input().split())
    G = list(map(int, input().split()))
    assert(len(G) == N)
    result = 0
    mod_counts = [0] * P
    for Gi in G:
        mod_counts[Gi % P] += 1

    #print(mod_counts, result)
    for group in groups[P]:
        #print('group:', group)
        while True:
            if all(m - g >= 0 for m, g in zip(mod_counts, group)):
                result += 1
                for i, g in enumerate(group):
                    mod_counts[i] -= g
                #print(mod_counts, result)
            else:
                break
    if sum(mod_counts) > 0:
        result += 1
    print('Case #{}: {}'.format(c + 1, result))

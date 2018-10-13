def split(gap):
    if gap % 2:
        return (gap-1)//2, (gap-1)//2
    else:
        return gap//2, gap//2 - 1

from collections import Counter

def stalls(n, k):
    multipliers = Counter()
    multipliers[n] += 1
    weight_queue = [(split(n), n)]
    processed = {n}
    while weight_queue:
        weight_queue.sort(
            key=lambda elem: elem[0],
            reverse=True
            )

        node, *weight_queue = weight_queue
        branches = node[0]

        k -= multipliers[node[1]]
        if k <= 0:
            return branches

        for v in branches:
            if v == 0:
                continue
            multipliers[v] += multipliers[node[1]]
            if v not in processed:
                weight_queue.append((split(v), v))
                processed.add(v)

dataset = []
with open('C-large.in') as in_file:
    for line in range(int(in_file.readline())):
        dataset += [tuple(map(int, in_file.readline().split()))]

results = []
for n, k in dataset:
    results += [stalls(n, k)]

with open('stalls_out.txt', 'w') as out:
    for i, r in enumerate(results):
        out.write(f'Case #{i+1}: {r[0]} {r[1]}\n')
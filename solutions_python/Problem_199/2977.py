#%%
with open("A-large.in") as fr:
    n = int(fr.readline())
    cakes = []
    K = []
    for i in range(n):
        line = fr.readline().split()
        cakes.append(line[0])
        K.append(int(line[1]))

    print(cakes, K)

def solutionA(cake, k):
    flip_count = 0
    cake_bool = [(True if c == '+' else False) for c in cake]
    for i in range(len(cake)-k+1):
        if not cake_bool[i]: # '-' case
            flip_count += 1
            for j in range(i, i+k):
                cake_bool[j] = not cake_bool[j]
    return flip_count if (False not in cake_bool) else -1

with open('ans.txt', 'w', encoding='utf8') as fw:
    for index, (c, k) in enumerate(zip(cakes, K), start=1):
        flip_times = solutionA(c, k)
        ans = "Case #{}: {}\n".format(index, flip_times if flip_times >= 0 else "IMPOSSIBLE")
        fw.write(ans)

"""
Output format:
Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE

"""

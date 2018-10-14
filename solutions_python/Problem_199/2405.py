import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    line = line.strip()

    pancakes, k = line.split()
    k = int(k)
    pancakes = [True if c == '+' else False for c in pancakes]
    flips = 0
    for ii in range(len(pancakes)-k+1):
        
        if not pancakes[ii]:
            flips += 1
            for j in range(ii, ii+k):
                pancakes[j] = not pancakes[j]

    if all(pancakes[len(pancakes)-k:]):
        print("Case #{}: {}".format(i, flips))
    else:
        print("Case #{}: IMPOSSIBLE".format(i))

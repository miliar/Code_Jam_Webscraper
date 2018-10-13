from collections import Counter
import fileinput


for e, line in enumerate(fileinput.input()):
    if fileinput.isfirstline():
        continue

    n, k = line.strip().split()
    gaps = Counter([int(n)])
    k = int(k)

    i = 0
    while i < k:
        gap = sorted(gaps.keys(), reverse=True)[0]
        count = gaps[gap]
        del gaps[gap]
        right = gap // 2
        left = gap - right - 1
        gaps[left] += count
        gaps[right] += count
        i += count

    print("Case #{}: {} {}".format(e, right, left))

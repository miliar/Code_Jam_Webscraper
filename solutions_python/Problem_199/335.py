def all_happy(pancakes):
    return all(pancake == '+' for pancake in pancakes)

n = int(raw_input())

for i in range(n):
    tmp = raw_input().split()
    pancakes = list(tmp[0])
    k = int(tmp[1])
    nflip = 0
    for j in range(0, len(pancakes) - k + 1):
        if pancakes[j] == '+':
            continue
        for p in range(k):
            if pancakes[j + p] == '-':
                pancakes[j + p] = '+'
            else:
                pancakes[j + p] = '-'
        nflip += 1

    if all_happy(pancakes):
        print "Case #{}: {}".format(i + 1, nflip)
    else:
        print "Case #{}: IMPOSSIBLE".format(i + 1)

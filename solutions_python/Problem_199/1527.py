T = int(input().strip())

for t in range(1, T+1):
    pancakes, k = input().strip().split(' ')
    pancakes = list(pancakes)
    k = int(k)
    # Brute force
    flips = 0
    for i in range(len(pancakes) - k + 1):
        if pancakes[i] == '+':
            continue
        flips += 1
        for j in range(i, i + k):
            if pancakes[j] == '-':
                pancakes[j] = '+'
            else:
                pancakes[j] = '-'
    good = True
    for p in pancakes:
        if p == '-':
            good = False
    if good:
        print('Case #%d: %d' % (t, flips))
    else:
        print('Case #%d: IMPOSSIBLE' % t)

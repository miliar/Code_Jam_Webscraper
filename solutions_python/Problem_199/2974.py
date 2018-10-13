t = int(raw_input())

for c in xrange(t):
    pancakes, k = raw_input().split()
    k = int(k)
    pancakes = list(pancakes)


    flips = 0
    for i in xrange(len(pancakes)):
        if pancakes[i] == '-' and i + k <= len(pancakes):
            flips += 1
            for j in xrange(i, i + k):
                if pancakes[j] == '-':
                    pancakes[j] = '+'
                else:
                    pancakes[j] = '-'

    valid = True
    for pancake in pancakes:
        if pancake == '-':
            valid = False
            break

    out = 'Case #%s: ' % (c + 1)
    if valid:
        print(out + str(flips))
    else:
        print(out + 'IMPOSSIBLE')
import fileinput

lines = list(fileinput.input())[1:]
for t, l in enumerate(lines):
    pancakes, k = l.split(' ')
    k = int(k)
    pancakes = list(pancakes)
    isHappy = lambda c: (c == '+')
    prevIsHappy = True
    flips = 0
    numPancakes = len(pancakes)
    impossible = False;
    for i in range(numPancakes - (k - 1)):
        if (pancakes[i] == '+'): continue
        flips = flips + 1
        for j in range(k):
            pancakes[i + j] = '-' if (pancakes[i + j] == '+') else '+'
    if ('-' in pancakes):
        result = 'IMPOSSIBLE'
    else: result = flips
    print "Case #{}: {}".format(t + 1, result)

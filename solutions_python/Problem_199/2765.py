def flip(stuff, index, fl):
    for i in range(fl):
        if stuff[index+i] == 0:
            stuff[index+i] = 1
        else:
            stuff[index+i] = 0
    return stuff


tests = int(input())

for z in range(tests):
    ins = input().split()
    cakes = [0 if x == '-' else 1 for x in ins[0]]
    flipper = int(ins[1])
    flips = 0
    i = 0
    while i <= len(cakes)-flipper:
        if cakes[i] == 0:
            cakes = flip(cakes, i, flipper)
            flips += 1
        i += 1
    if 0 in cakes:
        print("Case #{}: IMPOSSIBLE".format(z+1))
    else:
        print("Case #{}: {}".format(z+1, flips))

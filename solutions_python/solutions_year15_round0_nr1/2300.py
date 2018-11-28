T = int(input())
for case in range(T):
    line = input().split(' ')[1]
    standing  = 0
    shyness = 0
    added = 0
    for c in line:
        n = int(c)
        if shyness <= standing:
            standing += n
        else:
            added += abs(shyness - standing)
            standing += abs(shyness - standing)
            standing += n
        shyness += 1
    print("Case #{0}: {1}".format(case + 1, added))

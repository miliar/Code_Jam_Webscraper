def flip(pancakes):
    ret = ''
    for pancake in pancakes:
        if pancake == '+':
            ret = ret + '-'
        else:
            ret = ret + '+'
    return ret

t = int(input())
for i in range(1, t + 1):
    surface, length = input().split(" ")
    length = int(length)
    flips = 0

    for j in range(len(surface)-length + 1):
        if surface[j] == '-':
            surface = surface[:j] + flip(surface[j:j+length]) + surface[j + length:]
            flips += 1
    if '-' in surface:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        print("Case #{}: {}".format(i, flips))

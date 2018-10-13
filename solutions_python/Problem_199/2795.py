def flipPancakes(pancakes, k, pos):
    for x in range(pos, pos + k):
        if pancakes[x] == '+':
            pancakes = pancakes[:x] + '-' + pancakes[x+1:]
        else:
            pancakes = pancakes[:x] + '+' + pancakes[x+1:]
    return pancakes

def finishedPancake(pancakes):
    if pancakes == len(pancakes) * pancakes[0]:
        return True
    return False

t = int(input())

for i in range(1, t + 1):
    pancakes, k = [x for x in input().split(" ")]
    k = int(k)

    s = len(pancakes)

    flipCount = 0

    for x in range(0, s - k+1):
        if pancakes[x] == '-':
            pancakes = flipPancakes(pancakes, k, x)
            flipCount += 1

    if finishedPancake(pancakes):
        print ("Case #{0}: {1}".format(i, flipCount))
    else:
        print ("Case #{0}: IMPOSSIBLE".format(i))

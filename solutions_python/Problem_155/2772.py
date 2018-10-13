__author__ = 'ruben'

for t in range(int(input())):
    maxShy, shyStr = input().split()
    maxShy = int(maxShy)
    shyness = list(map(int, shyStr))
    #print(shyness)

    standing = 0
    needed = 0

    for shy, hesitant in enumerate(shyness):
        if standing < shy:
            neededExtra = shy - standing
            needed += neededExtra
            standing += neededExtra + hesitant
        else:
            standing += hesitant

    print("Case #{}: {}".format(t+1, needed))
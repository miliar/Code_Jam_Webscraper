from collections import OrderedDict
import math


def find_max(pancakes, k):
    sorted_pancakes = sorted(pancakes, key=lambda k: k["s"], reverse=True)
    #print("sorted: ", sorted_pancakes)
    max_area = -1
    for pancake in pancakes:
        _max = math.pi * pancake["r"] * pancake["r"] + 2 * math.pi * pancake["r"] * pancake["h"]
        i = 0
        flag = 1
        for sp in sorted_pancakes:
            if i == k - 1:
                break
            #print("enter with sp[{}]".format(sp))
            if sp["r"] == pancake["r"] and sp["h"] == pancake["h"] and flag:
                flag = 0
                continue
            _max += 2 * math.pi * sp["r"] * sp["h"]
            i += 1
        if _max > max_area:
            max_area = _max
    return max_area


def main():
    l = int(input())
    for i in range(0, l):
        inp = input().split(" ")
        n, k = int(inp[0]), int(inp[1])
        pancakes = []
        for j in range(0, n):
            l = input().split(" ")
            pancakes.append({"r": int(l[0]), "h": int(l[1]), "s": int(l[0]) * int(l[1])})
        max_area = find_max(pancakes, k)
        print("Case #{}: {}".format(i + 1, max_area))

main()
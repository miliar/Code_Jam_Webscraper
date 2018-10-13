import sys
sys.setrecursionlimit(1500)


def FindFlips(pancakes, start, k):

    end = len(pancakes)

    if start == end:
        return 0

    if end - start < k and pancakes[start] is False:
        return False

    flipped = 0

    if pancakes[start] is False:
        for i in range(k):
            pancakes[start+i] = not pancakes[start+i]
        flipped = 1

    num_flips = FindFlips(pancakes, start+1, k)
    if num_flips is False:
        if start == 0:
            return "IMPOSSIBLE"
        return False
    return num_flips + flipped


t = int(input())
i = 0

while t:
    t -= 1
    i += 1
    temp = input().split()
    pancakes = [True if x == '+' else False for x in temp[0]]
    k = int(temp[1])
    print("Case #{}: {}".format(i, FindFlips(pancakes, 0, k)))

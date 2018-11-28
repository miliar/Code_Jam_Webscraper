import math


def solve(stack):

    p = stack['p']
    k = stack['k']

    m = 0

    for x in p:
        tempS = list(p)
        tempS.remove(x)
        total = math.pi * x[0] * x[0] + x[2] + maxHeights(tempS, k - 1)
        if total > m:
            m = total

    return m

def maxHeights(p, k):

    heights = list(x[2] for x in p)

    return sum(sorted(heights, reverse = True)[:k])



def main():

    numToCheck = []

    for i in range(int(raw_input())):

        num, k = raw_input().split(' ')
        num = int(num)
        k = int(k)

        pancakes = []

        for i in range(num):
            r, h = raw_input().split(' ')
            r = int(r)
            h = int(h)
            pancakes.append([r, h, 2 * math.pi * r * h])

        numToCheck.append({"k": k, "p": pancakes})



    count = 0
    for pancakes in numToCheck:
        count += 1
        ret = solve(pancakes)

        print("Case #{}: {:.9f}".format(count, ret))


if __name__ == "__main__":
    main()
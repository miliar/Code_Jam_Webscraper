import math

def finalPosition(n, k):
    if k == 1:
        return (math.ceil((n-1)/2), math.floor((n-1)/2))
    if n % 2 == 1:
        return finalPosition(math.floor(n/2), math.ceil((k-1)/2))
    else:
        m = n / 2
        k = k - 1
        #go left as there is more space!
        if k % 2 == 1:
            return finalPosition(m, math.ceil(k/2))
        #go right
        else:
            return finalPosition(m-1, k/2)
        return "fdaa"


def freeStallsOnLeft(stalls, i):
    j = i-1
    while j>=0 and not(stalls[j]):
        j = j -1
    return i - j - 1 

def freeStallsOnRight(stalls, i):
    j = i+1
    while j<len(stalls) and not(stalls[j]):
        j = j + 1
    return j - i - 1

def bruteForce(n, k):
    stalls = [False for i in range(n)]
    while k >= 1:
        y = -1
        z = -1
        pos = -1
        for i in range(len(stalls)):
            if stalls[i]:
                continue
            left = freeStallsOnLeft(stalls, i)
            right = freeStallsOnRight(stalls, i)
            if min(left, right) > z:
                z = min(left, right)
                y = max(left, right)
                pos = i
            if min(left, right) == z:
                if max(left, right) > y:
                    y = max(left, right)
                    pos = i
        stalls[pos] = True
        k -= 1
    return y, z

t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    n, k  = [int(s) for s in input().split(" ")]
    y2, z2 = finalPosition(n, k)
    print("Case #{}: {} {}".format(i, y2, z2))

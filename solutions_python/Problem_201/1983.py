def stalls(n, k):
    best = [0, 0, 0]
    if n == k:
        return (0, 0, 0)
    s = [0 for i in range(0, n)]
    while k > 0:
        maximum = 0
        minimum = 0
        first = True
        for i in range(0,n):
            if s[i] == 0:
                left = 0
                right = 0
                for q in range(i-1,-1,-1):
                    if s[q] == 0:
                        left += 1
                    else:
                        break
                for r in range(i+1,n):
                    if s[r] == 0:
                        right += 1
                    else:
                        break
                if min(left, right) > minimum or first == True:
                    best = [i, min(left, right), max(left, right)]
                    maximum = best[2]
                    minimum = best[1]
                    first = False
                elif min(left, right) == minimum and max(left, right) > maximum:
                    best = [i, min(left, right), max(left, right)]
                    maximum = best[2]
                    minimum = best[1]
        s[best[0]] = 1
        k -= 1
    return best
                

t = int(input())
for i in range(1, t+1):
    n, k = [int(x) for x in input().split(" ")]
    b, Min, Max = stalls(n, k)
    print("Case #{}: {} {}".format(i, Max, Min))

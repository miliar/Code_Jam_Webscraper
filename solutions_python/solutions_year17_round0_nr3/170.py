def even(x):
    return x % 2 == 0

def odd(x):
    return x % 2 == 1

def solve(i):
    N, K = [int(x) for x in input().split(' ')]
    mymap = {N: 1}
    while K > 0:
        n = max(mymap)
        count = mymap[n]
        del mymap[n]
        if count >= K:
            if even(n):
                mymax = n // 2
                mymin = (n // 2) - 1
            else:
                mymax = mymin = (n - 1) // 2
            print("Case #{}: {} {}".format(i, mymax, mymin))
            return
        else:
            K -= count
            if n == 1:
                pass
            elif n == 2:
                if 1 not in mymap:
                    mymap[1] = 0
                mymap[1] += count
            elif even(n):
                if (n // 2) not in mymap:
                    mymap[n//2] = 0
                if ((n//2) - 1) not in mymap:
                    mymap[(n//2)-1] = 0
                mymap[n//2] += count
                mymap[(n//2)-1] += count
            else:
                if ((n - 1) // 2) not in mymap:
                    mymap[(n - 1) // 2] = 0
                mymap[(n - 1) // 2] += count + count


t = int(input())
for i in range(t):
    solve(i+1)
def pancakes(s,k):
    counter = 0
    for idx, cake in enumerate(s):
            counter += 1
    return counter

t = int(input())
for i in range(t):
    s,k = input().split()
    k = int(k)
    s = s.replace("-", "0")
    s = s.replace("+", "1")
    s = list(map(int,s))
    ans = pancakes(s,k)
    print("Case #{}: {}".format(i+1 , int(ans)))

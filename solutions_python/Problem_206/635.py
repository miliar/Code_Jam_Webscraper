
def solve(horses, dest):
    minSpeed = float("inf")
    for h in horses:
        time = (dest-h[0])/h[1]
        speed = dest/time
        if speed < minSpeed:
            minSpeed = speed

    return minSpeed


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    dest,n = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    horses = []
    for j in range(n):
        k,s = [int(s) for s in input().split(" ")]
        horses.append((k,s))
    ans = solve(horses,dest)
    print("Case #{}: {}".format(i, ans))
    # check out .format's specification for more formatting options


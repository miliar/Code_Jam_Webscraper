t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    d, n = [int(x) for  x in  input().split(" ")]  # read a list of integers, 2 in this case
    hs = []
    for i2 in range(0, n):
        k, s = [int(x) for x in  input().split(" ")]  # read a list of integers, 2 in this case
        hs.append((k, s))

    maxspeed = None
    for (k, s) in hs:
        curspeed = s * d / (d - k)
        if maxspeed == None or curspeed < maxspeed:
            maxspeed = curspeed


    print("Case #{}: {}".format(i, maxspeed))

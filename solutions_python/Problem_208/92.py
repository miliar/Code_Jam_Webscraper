def mintime(n, citydist, maxdist, speed):
    times = [0]
    for i in range(n-1, 0, -1):
        choices = []
        for j in range(n, i, -1):
            relv_dist = sum(citydist[(i-1):(j-1)])
            if relv_dist <= maxdist[i-1]:
                time = times[n-j] + relv_dist/speed[i-1]
                choices.append(time)
        best = min(choices)
        times.append(best)
    return times[-1]

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, q = input().split(" ")
    n = int(n)
    q = int(q)
    maxdist = []
    speed = []
    citydist = []
    for j in range(n):
        e, s = input().split(" ")
        e = int(e)
        s = int(s)
        maxdist.append(e)
        speed.append(s)
    for j in range(n):
        array = input().split(" ")
        if j != n-1:
            citydist.append(int(array[j+1]))
    u, v = input().split(" ")
    result = mintime(n, citydist, maxdist, speed)
    print("Case #{}: {}".format(i, result))

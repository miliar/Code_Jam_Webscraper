import math

t = int(input())
for i in range(1, t+1):
    line = input()
    d = int(line.split(" ")[0])
    n = int(line.split(" ")[1])
    max_t = 0
    for j in range(n):
        line = input()
        k = int(line.split(" ")[0])
        s = int(line.split(" ")[1])
        max_t = max(max_t, (d - k) / s)
    v_max = d/max_t
    print("Case #{}:".format(i), "{0:.6f}".format(v_max))
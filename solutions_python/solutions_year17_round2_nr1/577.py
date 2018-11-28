filename = input()
f = open(filename + ".in")
o = open(filename + ".out", "w")
T = int(f.readline())

for t in range(1, T + 1):
    D, N = list(map(int, f.readline().split()))
    last_time = 0
    for i in range(0, N):
        K, S = list(map(int, f.readline().split()))
        i_time = (D - K) / S
        if i_time > last_time:
            last_time = i_time
    speed = D / last_time
    print("Case #" + str(t) + ": " + str(speed))
    o.write("Case #" + str(t) + ": " + str(speed) + "\n")
f.close()
o.close()

ret = []
with open('A-large.in', 'r') as file:
    t = int(file.readline())
    for __ in range(t):
        d, n = map(int, file.readline().split())
        slowest = 0
        for horse in range(n):
            k, s = map(int, file.readline().split())
            time = (d-k)/s
            if slowest < time:
                slowest = time
        ret.append(d/slowest)


with open('Aout-large.txt', 'w') as outfile:
    for i in range(t):
        outfile.write("Case #%d: %s\n" %(i+1, ret[i]))
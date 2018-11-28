from collections import deque

f = open("C-small-attempt0.in")

T = int(f.readline())

out = open("C-small.out", 'w')

for i in range(T):
    R, k, N = [int(x) for x in f.readline().split()]
    groups = deque([int(x) for x in f.readline().split()])

    profit = 0
    for j in range(R):
        c = 0
        for count in range(len(groups)):
            x = groups[0]
            if c + x <= k:
                groups.append(groups.popleft())
                c += x

            else:
                break
        profit += c

    out.write("Case #%d: %d\n" % (i+1, profit))

f.close()
out.close()
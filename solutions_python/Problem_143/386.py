f = open("data.txt", 'r')
g = open("data1.txt", 'w')
t = int(f.readline())
for i in range(1, t+1):
    A, B, K = [int(x) for x in f.readline().split()]
    result = 0
    for p in range(A):
        for q in range(B):
            if p&q < K:
                result += 1
    g.write("Case #%d: %d\n" % (i, result))
f.close()
g.close()
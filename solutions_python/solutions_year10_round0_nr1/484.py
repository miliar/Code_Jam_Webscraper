f = open("A-large.in")

T = int(f.readline())

out = open("A-large.out", 'w')

for i in range(T):
    N, K = [int(x) for x in f.readline().split()]
    q = 2**N
    a = (K - q + 1)/float(q)
    if not a % 1:
        out.write("Case #%d: ON\n" % (i+1))
    else:
        out.write("Case #%d: OFF\n" % (i+1))

out.close()
f.close()
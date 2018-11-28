f = file("A-large.in")
a = f.readlines()
N = int(a.pop(0).strip())
for i in range(N):
    n, k = [int(tmp) for tmp in a.pop(0).strip().split(" ")]
    if (k+1) % 2**n == 0:
        print "Case #" + str(1+i) + ": ON"
    else:
        print "Case #" + str(1+i) + ": OFF"
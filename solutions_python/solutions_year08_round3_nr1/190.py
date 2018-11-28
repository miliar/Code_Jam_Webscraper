f = open("A-small-attempt0.in")
out = open ("A-small-attempt0.out", "w")

N = int(f.readline().strip())

for i in xrange(1, N+1):
    S = map(int, f.readline().strip().split(" "))
    
    P = S[0]
    K = S[1]
    L = S[2]

    freq = map(int, f.readline().strip().split(" "))

    freq.sort()
    freq.reverse()

    keysUsed = 0
    km = 0
    keyPresses = 0

    for X in freq:
        keysUsed += 1
        if keysUsed % K == 1:
            km += 1
        keyPresses += X * km

    out.write("Case #" + str(i) + ": " + str(keyPresses) + "\n")

out.flush()
out.close()
f.close()

    

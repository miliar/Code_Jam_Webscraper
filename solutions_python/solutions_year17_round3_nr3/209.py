def change(probs, i, total, N):
    newP = total / ((N - i) * 1.0)
    for j in range(i, N):
        probs[j] = newP

fileName = "C-small-1-attempt0.in"
f = open(fileName, 'r')

outputName = "C-small-0-0-out.txt"
output = open(outputName, 'w')

line = f.readline()
T = int(line)

for t in range(T):
    res = ""
    
    N, K = map(int, f.readline().split())
    U = float(f.readline())
    probs = list(map(float, f.readline().split()))
    
    probs.sort(reverse = True)
    
    for i in range(N):
        total = U
        for j in range(i, N):
            total += probs[j]
        if (total / ((N - i) * 1.0)) >= probs[i]:
            change(probs, i, total, N)
            break
#
    ans = 1.0
    print probs
    for p in probs:
        ans = ans * p
#    
    res = "{0:.9f}".format(ans)
        
    print("Case #{}: {}".format(t+1, res))
    output.write("Case #{}: {}".format(t+1, res))
    output.write("\n")
    
output.close()
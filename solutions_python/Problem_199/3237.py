
fin = open('pancake.in','r')
fout = open('pancake.out','w')

T = int(fin.readline())
for t0 in range(T):
    pancakes, K = fin.readline().split()
    K = int(K)

    pancakes = list(pancakes)
    ans = 0
    for i in range(len(pancakes) - K + 1):
        if pancakes[i] == "-":
            for j in range(K):
                pancakes[i+j] = "+" if pancakes[i+j] == "-" else "-"
            ans += 1
        #print pancakes

    worked = True
    for i in range(len(pancakes)):
        if pancakes[i] != "+":
            worked = False
            break

    fout.write("Case #" + str(t0 + 1) + ": " + (str(ans) if worked else "IMPOSSIBLE") + "\n")

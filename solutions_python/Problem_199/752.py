fin = open("A.in")
fout = open("A.out", "w")
T = int(fin.readline())

def success(t, n):
    fout.write("Case #"+str(t+1) + ": " + str(n) + "\n")

def fail():
    fout.write("Case #"+str(t+1) + ": IMPOSSIBLE\n")

for t in range(T):
    pancakes, K = fin.readline().split()
    pancakes = list(pancakes)
    K = int(K)
    count = 0
    if '-' not in pancakes:
        success(t, count)
        continue

    for i in range(len(pancakes) - K + 1):
        if pancakes[i] is '-':
            for j in range(i, i+K):
                if pancakes[j] is '-':
                    pancakes[j] = '+'
                else:
                    pancakes[j] = '-'
            count += 1
    if '-' not in pancakes:
        success(t, count)
        continue
    else:
        fail()
        continue



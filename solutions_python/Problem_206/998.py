outputPath = "C:\\Users\\Oliver\\OneDrive\\Documents\\Code\\Google Code Jam 2017\\output.txt"

def write(s):
    with open(outputPath, 'a') as f:
        f.write(s + "\n")
    print(s)

def getMaxSpeed(d, ks, ss):
    maxTime = 0
    for i in range(len(ks)):
        time = (d - ks[i]) / ss[i]
        if maxTime < time:
            maxTime = time
    return d / maxTime

open(outputPath, 'w').close()
t = int(input())
for i in range(1, t+1):
    d_n = input().split(' ')
    d = int(d_n[0])
    n = int(d_n[1])
    ks = []
    ss = []
    for j in range(n):
        k_s = input().split(' ')
        ks.append(int(k_s[0]))
        ss.append(int(k_s[1]))
    write("Case #" + str(i) + ": " + str(getMaxSpeed(d, ks, ss)))

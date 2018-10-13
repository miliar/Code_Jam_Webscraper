import math

TASK = "B-large"
FIN = open(TASK + ".in")
FOUT = open(TASK + ".out", "w")

t = int(FIN.readline())
# t = int(input())
for _ in range(1, t + 1):
    s = FIN.readline()
    s = s[0: len(s) - 1]
    # s = input()
    k = len(s)
    for i in range(1, k):
        if int(s[i]) < int(s[i - 1]):
            j = i
            while j > 0:
                if int(s[j]) < int(s[j - 1]):
                    z = int(s[j - 1])
                    s = s[0: j - 1] + str(z - 1) + s[j:]
                    j -= 1
                else:
                    break
            s = s[0: j + 1]
            for z in range(j + 1, k):
                s += "9"
            break
    if s[0] == "0":
        s = s[1:]
    ans = "Case #" + str(_) + ": " + s
    print(ans, file = FOUT)

FIN.close()
FOUT.close()

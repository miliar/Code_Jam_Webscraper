import sys
T = sys.stdin.readline()
for i, line in enumerate(sys.stdin):
    s, k = line.split(" ")
    k = int(k)
    s = list(s)
    n = 0
    if k > 0:
        for j in range(len(s)-k+1):
            if s[j] == "-":
                n+=1
                for a in range(j,j+k):
                    if s[a] == "-":
                        s[a] = '+'
                    else:
                        s[a] = "-"


        for b in range(1, k):
             if s[-b] == "-":
                 n = "IMPOSSIBLE"

    else:
        for b in range(0, len(s)):
             if s[b] == "-":
                 n = "IMPOSSIBLE"


    print("CASE #{}: {}".format(i+1, n))
    if T == i+1:
        break

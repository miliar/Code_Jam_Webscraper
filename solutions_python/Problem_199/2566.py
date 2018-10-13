f = open('output.txt', 'w')
T = int(input())

for i in range(T):
    flips = 0
    line = input()
    a = line.split(" ")
    a[1] = int(a[1])
    S = list(a[0])
    K = a[1]
    possible = True
    incomplete = True
    if S == '+' * len(S):
        incomplete = False
    while(possible and incomplete):
        for j in range(len(S) - K + 1):
            if(S[j] == "-"):
                flips += 1
                for k in range(j, j + K):
                    if S[k] == "-":
                        S[k] = "+"
                    else:
                        S[k] = "-"
        incomplete = False
        for j in range(len(S)):
            if S[j] != S[j-1] and j > len(S) - K:
                possible = False
                break;
            if S[j] == "-":
                incomplete = True


    if possible:
        f.write("Case #" + str(i+1) + ": " + str(flips) + "\n")
    else:
        f.write("Case #" + str(i+1) + ": IMPOSSIBLE\n")

f.close()

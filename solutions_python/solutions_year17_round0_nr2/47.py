N = int(input())
for j in range(N):
    line = input()
    out = ""
    retenue = 0
    for i in range(len(line) - 1, 0, -1):
        if int(line[i]) - retenue < int(line[i - 1]) or int(line[i]) - retenue == -1:
            retenue = 1
            out = "9" * (len(out) + 1)
        else:
            out = str(int(line[i]) - retenue) + out
            retenue = 0
    out = str(int(line[0]) - retenue) + out
    while out[0] == "0":
        out = out[1:]
    print("Case #{}:".format(j+1),out)

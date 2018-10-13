t = int(input())
def done(slist):
    for i in range(0, len(slist)):
        if slist[i] == "-":
            return False
    return True
for test in range(0, t):
    cur = input()
    curl = cur.split(" ")
    s = curl[0]
##    print(s)
    sl = list(s)
    k = int(curl[1])
    count = 0
    for i in range(0, len(sl)-k+1):
        if sl[i] == "-":
            for j in range(i, i+k):
                if sl[j] == "-":
                    sl[j] = "+"
                else:
                    sl[j] = "-"
            count += 1
    if done(sl):
        print("Case #" + str(test+1) + ": " + str(count))
    else:
        print("Case #" + str(test+1) + ": " + "IMPOSSIBLE")
##    print(sl, k)
##    print(count)

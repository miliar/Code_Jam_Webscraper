x = int(input())
for w in range(x):
    q = int(input())
    tmp = 0
    i = 0
    while i < len(str(q)):
        if int(str(q)[i]) >= tmp:
            tmp = int(str(q)[i])
            i += 1
        else:
            q -= (int(str(q)[i:]) + 1)
            tmp = 0
            i = 0
    print ("Case #" + str(w+1) + ": " + str(q))


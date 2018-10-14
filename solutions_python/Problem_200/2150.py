x = open("B-large.in")
z = open("B-large.out", "w")
n = int(x.readline()[:-1])
zs = ""

for i in range(n):
    l = []
    y = x.readline()[:-1]
    if y == "":
        break
    else:
        if len(y) == 1:
            zs += "Case #" + str(i + 1) + ": " + y + "\n"
        else:
            for j in y:
                print(j)
                l.append(int(j))
            for j in range(1, len(l)):
                if int(l[-j]) < int(l[-j-1]):
                    l[-j] = 9
                    if l[-j-1] != 0:
                        l[-j-1] -= 1
                    else:
                        k = 1
                        while 1:
                            l[-j-k] = 9
                            k += 1
                            if l[-j-k] != 0:
                                l[-j-k] -= 1
                                break
                    for m in range(1, j):
                        l[-m] = 9
            y = ""
            for j in l:
                y += str(j)
            y = int(y)
            zs += "Case #" + str(i + 1) + ": " + str(y) + "\n"

z.write(zs[:-1])
z.close()

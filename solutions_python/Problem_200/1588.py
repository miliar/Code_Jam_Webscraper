def problem2():
    f = open("B-small-attempt0.in", "r")
    f2 = open("B-small-attempt0.out", "w")
    line = f.readline()
    for i in range(1, int(line.strip())+1):
        num = int(f.readline().strip())
        if num < 10:
            f2.write("Case #" + str(i) + ": " + str(num) + "\n")
        else:
            numStr = list(str(num))
            maxL = len(numStr) - 1
            l = maxL
            while l != 0:
                if int(numStr[l]) < int(numStr[l-1]):
                    numStr[l-1] = str(int(numStr[l-1])-1)
                    for i2 in range(l,maxL+1):
                        numStr[i2] = "9"
                l -= 1
            if numStr[0] == "0":
                del numStr[0]
            s = ""
            for d in numStr:
                s+= d
            f2.write("Case #" + str(i) + ": " + s + "\n")
    f.close()
    f2.close()


problem2()

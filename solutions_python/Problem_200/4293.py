def findtidy(num):
    numstr = str(num)
    l = len(numstr)
    if l == 1:
        return num
    else:
        pos = 0
        posassigned = False
        for i in range(l - 1):
            j = numstr[i:i+1]
            k = numstr[i+1:i+2]
            if (j < k):
                pos = i + 1
            elif (j == k):
                if posassigned == False:
                    pos = i
                    posassigned = True
            elif (j > k):
                res = numstr[:pos] + str((long(numstr[pos:pos+1]) - 1))
                lres = len(res)
                res = res + "".ljust((l - lres),"9")
                return long(res)
    return num

def tidynum(filename = "d:\\codejam\\B-large.in"):
    linecount = 0
    ntestcase = 0
    res = ""
    filenameout = "d:\\codejam\\B-large.out"
    with open(filename,"rb") as f:
        for line in f:
            if linecount == 0:
                ntestcase = line.rstrip("\r\n")
                linecount = linecount + 1
            else:
                num = long(line.rstrip("\r\n"))
                num = findtidy(num)
                res = res + "Case #" + str(linecount) + ": " + str(num) + "\n"
                linecount = linecount + 1
    with open(filenameout,"wb") as f1:
        f1.write(res)



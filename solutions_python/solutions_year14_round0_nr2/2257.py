
files = open("./bl.in")

num = 0
probNum = 0
flag = False
for line in files:
    num = num + 1
    if num == 1:
        probNum = int(line)
        continue
    bit = line.rsplit()
    c = float(bit[0])
    f = float(bit[1])
    x = float(bit[2])

    #print c, f, x, " ",
    incr = 2.0
    minTime = x / incr
    baseTime = 0
    while True:
        baseTime +=  c / incr
        incr += f
        newMinTime = baseTime + (x / incr)
        if minTime <= newMinTime:
            break
        minTime = newMinTime

    string = "Case #" + str(num - 1) + ": "
    print string + str(round(minTime, 7))

"""
    if (k % pow(2, n)) == (pow(2, n) - 1):
    flag = True
    else:
    flag = False

    string = "Case #" + str(num - 1) + ": "
    if flag == False:
    string = string + "OFF\n"
    else:
    string = string + "ON\n"
    print string
"""
files.close()

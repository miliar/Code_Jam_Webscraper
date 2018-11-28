def Cookie(filename):
    f = open(filename,"r")
    casenumberStr = f.readline()
    casenumberSplit = casenumberStr.split()
    casenumber = int(casenumberSplit[0])
    for i in range(casenumber):
        aline = f.readline()
        numbers = aline.split()
        cost = float(numbers[0])
        bNumber = float(numbers[1])
        goal = float(numbers[2])
        time = 0
        counter = 0
        nTh = goal/(2+counter*bNumber)
        mTh = cost/(2+counter*bNumber)+goal/(2+(counter+1)*bNumber)
        while nTh > mTh:
            time = time+ cost/(2+counter* bNumber)
            counter = counter + 1
            nTh = goal/(2+counter * bNumber)
            mTh = cost/(2+counter * bNumber) + goal/(2+(counter + 1)*bNumber)
        time = time + goal/(2+counter * bNumber)
        timeStr = "{:.7f}".format(time)
        output = "Case #{}: ".format(i+1) + timeStr
        print(output)
    f.close()



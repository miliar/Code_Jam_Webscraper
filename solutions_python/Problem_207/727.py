def solve(s):
    lis = map(int,s.split(" "))
    n = lis[0]
    # n = sum(lis)
    newlis = lis[1:]
    newlis[0] += lis[2] + lis[6]  # red
    newlis[2] += lis[2] + lis[4]  # yellow
    newlis[4] += lis[4] + lis[6]  # blue
    # newlis[1] += lis[1] + lis[3]  # orange
    # newlis[3] += lis[3] + lis[5]  # green
    # newlis[5] += lis[1] + lis[5] # violet
    charList = ['R','O','Y','G','B','V']
    # print newlis
    if max(newlis)>n/2:
        return "IMPOSSIBLE"
    else:
        sortedList = sorted(range(len(newlis)), key=lambda k: newlis[k],reverse=True)
        # print newlis
        # print sortedList
        string = ''
        expected = ['']*n
        global start
        start = 0

        def calc(a,x):
            global start
            while a:
                a -= 1
                lis[x] -= 1
                # print expected
                expected[start] = charList[x - 1]
                if start + 2 > n - 1:
                    start = 1
                else:
                    start +=2


        for i in sortedList:
            if i==0:
                a, b, c = lis[1],lis[2],lis[6]
                calc(a,1)

                if b>c:
                    calc(b, 2)
                    calc(lis[3], 3)
                    calc(lis[5], 5)
                    calc(c, 6)
                else:
                    calc(c, 6)
                    calc(lis[5], 5)
                    calc(lis[3], 3)
                    calc(b, 2)
            if i==2:
                a, b, c = lis[3], lis[2], lis[4]
                calc(a, 3)

                if b>c:
                    calc(b, 2)

                    calc(lis[1], 1)
                    calc(lis[5], 5)
                    calc(c, 4)
                else:
                    calc(c, 4)
                    calc(lis[5], 5)
                    calc(lis[1], 1)
                    calc(b, 2)

            if i ==4:
                a, b, c = lis[5], lis[4], lis[6]
                calc(a, 5)

                if b>c:
                    calc(b, 4)
                    calc(lis[3], 3)
                    calc(lis[1], 1)
                    calc(c, 6)
                else:
                    calc(c, 6)
                    calc(lis[1], 1)
                    calc(lis[3], 3)
                    calc(b, 4)
            if i==1:
                a, b, c = lis[2], lis[1], lis[3]
                calc(a, 2)
                calc(b, 1)
                calc(c, 3)
            if i ==3:
                a, b, c = lis[4], lis[3], lis[5]
                calc(a, 4)
                calc(b, 3)
                calc(c, 5)
            if i==5:
                a, b, c = lis[6], lis[1], lis[5]
                calc(a, 6)
                calc(b, 1)
                calc(c, 5)

        return "".join(expected)


if __name__=="__main__":
    t = int(raw_input().strip())
    case = 0
    while case < t:
        case += 1
        s = raw_input().strip()
        print "Case #" + str(case) + ":",solve(s)


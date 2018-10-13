def parse(fi):
    f = open(fi,"r")
    return map(lambda x: x[:-1],f.readlines())

def p2():
    data = parse("problem2/input.txt")
    data = map(lambda x: map(lambda y: int(y),x.split()),data)
    for count in range(1,1+data[0][0]):
        n = data[count][0]
        red = data[count][1]
        yellow =  data[count][3]
        blue = data[count][5]
        if red > n/2 or yellow > n/2 or blue > n/2:
            print "Case #" + str(count) + ": IMPOSSIBLE"
        else:
            s = ""
            for j in range(n):
                if red > yellow and red > blue and (s == "" or s[-1] != 'R') and red > 0:
                    s += "R"
                    red -= 1
                elif yellow > red and yellow > blue and (s == "" or s[-1] != 'Y') and yellow > 0:
                    s += "Y"
                    yellow -= 1
                elif blue > yellow and blue > red and (s == "" or s[-1] != 'B') and blue > 0:
                    s += "B"
                    blue -= 1
                # elif (red > yellow or red > blue) and (s == "" or s[-1] != 'R') and red > 0:
                #     s += "R"
                #     red -= 1
                # elif (yellow > red or yellow > blue) and (s == "" or s[-1] != 'Y') and yellow > 0:
                #     s += "Y"
                #     yellow -= 1
                # elif (blue > yellow or blue > red) and (s == "" or s[-1] != 'B') and blue > 0:
                #     s += "B"
                #     blue -= 1
                elif (s == "" or s[-1] != 'R') and red > 0 and data[count][1] >= data[count][3] and data[count][1] >= data[count][5]:
                    s += "R"
                    red -= 1
                elif (s == "" or s[-1] != 'Y') and yellow > 0 and data[count][3] >= data[count][1] and data[count][3] >= data[count][5]:
                    s += "Y"
                    yellow -= 1
                elif (s == "" or s[-1] != 'B') and blue > 0 and data[count][5] >= data[count][1] and data[count][5] >= data[count][3]:
                    s += "B"
                    blue -= 1
                elif (s == "" or s[-1] != 'R') and red > 0:
                    s += "R"
                    red -= 1
                elif (s == "" or s[-1] != 'Y') and yellow > 0:
                    s += "Y"
                    yellow -= 1
                elif (s == "" or s[-1] != 'B') and blue > 0:
                    s += "B"
                    blue -= 1
                else:
                    return
                if len(s) >= 2 and s[-2] == s[-1]:
                    return

            if s.count('Y') != data[count][3] or s.count('R') != data[count][1] or s.count('B') != data[count][5]:
                print s
                return
            if s[0] == s[-1]:
                print s
                return
            print "Case #" + str(count) + ": " + s




p2()

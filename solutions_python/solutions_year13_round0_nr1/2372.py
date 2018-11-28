for test in range(input()):
    res = ["X won","O won","Draw","Game has not completed"]

    inp = []
    #print "i",len(inp)

    while len(inp) < 4:
        i = raw_input()
        if i  != "":
            inp.append(i)


    flag = 1

    #print inp

    
    for i in inp: 
        if i == "OOOO" or  i == "TOOO" or i == "OTOO" or i == "OOTO" or i == "OOOT":
            n = 1
            flag = 0
        elif i == "XXXX" or i == "TXXX" or i == "XTXX" or i == "XXTX" or i == "XXXT":
            n = 0
            flag = 0
    
    
        
    if flag == 1:
        for i in range(4):
            a = inp[0][i] + inp[1][i] + inp[2][i] + inp[3][i]
            if a == "OOOO" or  a == "TOOO" or a == "OTOO" or a == "OOTO" or a == "OOOT":
                n = 1
                flag = 0
            elif a == "XXXX" or a == "TXXX" or a == "XTXX" or a == "XXTX" or a == "XXXT":
                n = 0
                flag = 0

    if flag == 1:
        a = inp[0][0] + inp[1][1] + inp[2][2] + inp[3][3]
        if a == "OOOO" or  a == "TOOO" or a == "OTOO" or a == "OOTO" or a == "OOOT":
            n = 1
            flag = 0
        elif a == "XXXX" or a == "TXXX" or a == "XTXX" or a == "XXTX" or a == "XXXT":
            n = 0
            flag = 0

    if flag == 1:
        b = inp[0][3] + inp[1][2] + inp[2][1] + inp[3][0]
        if b == "OOOO" or  b == "TOOO" or b == "OTOO" or b == "OOTO" or b == "OOOT":
            n = 1
            flag = 0
        elif b == "XXXX" or b == "TXXX" or b == "XTXX" or b == "XXTX" or b == "XXXT":
            n = 0
            flag = 0


    if flag == 1:
        for i in inp:
            if "." in i:
                n = 3
                flag = 0
    
    if flag == 1:
        n = 2
    
    print "Case #%d:"%(test + 1),res[n]

def main():
    t = int(raw_input())
    for i in range(0, t):
        output = ""
        count = 0
        xwin = False
        owin = False
        str = {}
        for j in range(0, 4):
            str[j] = raw_input()
            for k in xrange(4):
                if str[j][k] != '.':
                    count += 1
        for j in range(0, 4):
            valx = 0
            valo = 0
            val = 0
            for k in range(0, 4):
                if str[j][k] == 'X':
                    valx += 1
                elif str[j][k] == 'O':
                    valo += 1
                elif str[j][k] == 'T':
                    val += 1
            if valx + val == 4:
                xwin = True
            if valo + val == 4:
                owin = True
        for j in range(0, 4):
            valx = 0
            valo = 0
            val = 0
            for k in range(0, 4):
                if str[k][j] == 'X':
                    valx += 1
                elif str[k][j] == 'O':
                    valo += 1
                elif str[k][j] == 'T':
                    val += 1
            if valx + val == 4:
                xwin = True
            if valo + val == 4:
                owin = True
        valx = 0
        valo = 0
        val = 0
        for j in range(0, 4):
            if str[j][j] == 'X':
                valx += 1
            elif str[j][j] == 'O':
                valo += 1
            elif str[j][j] == 'T':
                val += 1
        if valx + val == 4:
            xwin = True
        if valo + val == 4:
            owin = True
        valx = valo = val = 0
        for j in range(0, 4):
            if str[j][4 - j - 1] == 'X':
                valx += 1
            elif str[j][4 - j - 1] == 'O':
                valo += 1
            elif str[j][4 - j - 1] == 'T':
                val += 1
        if valx + val == 4:
            xwin = True
        if valo + val == 4:
            owin = True
        if xwin:
            output = "X won"
        elif owin:
            output = "O won"
        elif count != 16:
            output = "Game has not completed"
        else:
            output = "Draw"
        print "Case #%s: %s" % (i + 1, output)
        raw_input()
main()

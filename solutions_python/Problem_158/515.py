if __name__ == "__main__":
    with open("D.in") as f:
        cnt = 0
        num_cases = int(f.readline())
        for i in xrange(num_cases):
            x, r, c = f.readline().split()
            x = int(x)
            r = int(r)
            c = int(c)

            if x == 1:
                ret = "GABRIEL"
            elif x == 2:
                if r == 1 and c == 1:
                    ret = "RICHARD"
                else:
                    if (r * c) % 2 == 0:
                        ret = "GABRIEL"
                    else:
                        ret = "RICHARD"
            elif x == 3:
                if r <= 2 and c <= 2:
                    ret = "RICHARD"
                elif (r == 3 and c == 1) or (r == 1 and c == 3):
                    ret = "RICHARD"
                elif (r == 3 and c == 2) or (r == 2 and c == 3):
                    ret = "GABRIEL"
                elif (r == 3 and c == 3):
                    ret = "GABRIEL"
                elif (r == 4 and c == 1) or (r == 1 and c == 4):
                    ret = "RICHARD"
                elif (r == 4 and c == 2) or (r == 2 and c == 4):
                    ret = "RICHARD"
                elif (r == 4 and c == 3) or (r == 3 and c == 4):
                    ret = "GABRIEL"
                elif (r == 4 and c == 4):
                    ret = "RICHARD"
            elif x == 4:
                if r <= 3 and c <= 3:
                    ret = "RICHARD"
                elif (r == 4 and c == 1) or (r == 1 and c == 4):
                    ret = "RICHARD"
                elif (r == 4 and c == 2) or (r == 2 and c == 4):
                    ret = "RICHARD"
                elif (r == 4 and c == 3) or (r == 3 and c == 4):
                    ret = "GABRIEL"
                elif (r == 4 and c == 4):
                    ret = "GABRIEL"

            print "Case #%s: %s" % (i + 1, ret)


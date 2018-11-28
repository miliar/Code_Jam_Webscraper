m = int(1)
def display(n):
        global m
        print("Case #"+str(m)+": %.7f" % n)
        m = m+1
for t in range(input()):
    c, f, x = raw_input().split()
    c, f, x, y, r = float(c), float(f), float(x), list(), int(2)
    if x<c:
        y = x/r
        display(y)
    else:
        while True:
                y1 = float(c)/r
                r = r + f
                y2 = x/r
                yc = y1 + y2
                yx = float(x)/(r-f)
                if yx < yc:
                        y.append(yx)
                        display(sum(y))
                        break
                else:
                        y.append(y1)

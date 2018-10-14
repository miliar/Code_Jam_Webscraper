inp = open('D-small.in', 'r')
out = open('D-small.out', 'w')

def single():
    return inp.readline().strip()

def mult():
    return inp.readline().strip().split()

def multint():
    x = inp.readline().strip().split()
    for a in range(len(x)):
        x[a] = int(x[a])
    return x

def omino(xrc):
    x, r, c = int(xrc[0]), int(xrc[1]), int(xrc[2])

    if x > r and x > c:
        return "RICHARD"
    if x == 3:
        if (r == 3 and c == 1) or (r == 1 and c == 3):
            return "RICHARD"

    if x == 4:
        if (r == 4 and c == 1) or (r == 1 and c == 4):
            return "RICHARD"

        if (r == 4 and c == 2) or (r == 2 and c == 4):
            return "RICHARD"

    if (r*c-x) % x != 0:
        return "RICHARD"
    else:
        return "GABRIEL"

cases = int(inp.readline().strip())

for r in range(cases):

    xrc = mult()

    result = omino(xrc)

    print("Case #" + str(r+1) + ": " + result)
    out.write("Case #" + str(r+1) + ": " + result + "\n")    

inp.flush()
out.flush()
inp.close()
out.close()

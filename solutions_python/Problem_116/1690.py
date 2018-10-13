# ticTacToeTomek.py


def main():
    num = raw_input()
    problist = []
    
    for a in range(int(num)):
        thisprob = []
        for a in range(4):
            thisprob.append(raw_input())
        problist.append(thisprob)
        raw_input()
    
    for (pos,a) in enumerate(problist):
        print "Case #%d: %s"%(pos+1,judgeBoard(a))

def judgeBoard(inlist):
    for x in range(4):
        if all(inlist[x][y] in "XT" for y in range(4)):
            return "X won"
        if all(inlist[y][x] in "XT" for y in range(4)):
            return "X won"
    for x in range(4):
        if all(inlist[x][y] in "OT" for y in range(4)):
            return "O won"
        if all(inlist[y][x] in "OT" for y in range(4)):
            return "O won"
    
    if all(inlist[y][y] in "OT" for y in range(4)):
        return "O won"
    if all(inlist[y][y] in "XT" for y in range(4)):
        return "X won"
    if all(inlist[y][3-y] in "OT" for y in range(4)):
        return "O won"
    if all(inlist[y][3-y] in "XT" for y in range(4)):
        return "X won"
        
    if '.' not in "".join(inlist):
        return "Draw"
    return "Game has not completed"


if __name__ == "__main__":
    main()
        

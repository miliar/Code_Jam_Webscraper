
f = open("C:\\Users\\TocarIP\\Google Drive\\Downloads\\B-small-attempt1.in")
#f = open("C:\\Users\\TocarIP\\Google Drive\\Downloads\\qaz.txt")
lines = f.readlines()
numcases = int(lines[0])
i = 1
pos = 1
while i <= numcases:
    res = "Case #" + str(i) + ": "
    n,r,o,y,g,b,v = [int(x) for x in lines[pos].split()]
    if o != 0:
        b -= o
        if b < 0:
            print(res + "IMPOSSIBLE")
            i = i + 1
            pos += 1
            continue
        if b == 0:
            if r !=0 or y != 0 or g != 0 or v != 0:
                print(res + "IMPOSSIBLE")
            else:
                print(res + "BO" * o)
            i = i + 1
            pos += 1
            continue
    if g != 0:
        r -= g
        if r < 0:
            print(res + "IMPOSSIBLE")
            i = i + 1
            pos += 1
            continue
        if r == 0:
            if o !=0 or y != 0 or b != 0 or v != 0:
                print(res + "IMPOSSIBLE")
            else:
                print(res + "RG" * g)
            i = i + 1
            pos += 1
            continue
    if v != 0:
        y -= v
        if y < 0:
            print(res + "IMPOSSIBLE")
            i = i + 1
            pos += 1
            continue
        if y == 0:
            if r !=0 or o != 0 or g != 0 or b != 0:
                print(res + "IMPOSSIBLE")
            else:
                print(res + "YV" * v)
            i = i + 1
            pos += 1
            continue
    sol = ""
    if r >= y and r >= b:
        r -=1
        sol += "R"
    elif y >= r  and y >= b:
        y -= 1
        sol +="Y"
    else:
        b-=1
        sol += "B"
    while r + y + b > 0:
        last = sol[len(sol) - 1]
        if last == "R" and y == 0 and b == 0:
            sol = "IMPOSSIBLE"
            break
        if last == "Y" and r == 0 and b == 0:
            sol = "IMPOSSIBLE"
            break
        if last == "B" and y == 0 and r == 0:
            sol =  "IMPOSSIBLE"
            break
        if last == "R" and y > b:
            y -= 1
            sol +="Y"
        elif last == "R" and b > y:
            b -= 1
            sol +="B"
        elif last == "R" and b == y:
            if sol[0] == "B":
                sol +="B"
                b -= 1
            else:
                sol += "Y"
                y -= 1
        elif last == "Y" and r > b:
            r -= 1
            sol +="R"
        elif last == "Y" and b > r:
            b -= 1
            sol +="B"
        elif last == "Y" and r == b:
            if sol[0] == "R":
                sol += "R"
                r -=1
            else:
                sol += "B"
                b -= 1
        elif last == "B" and r > y:
            r -= 1
            sol += "R"
        elif last == "B" and y > r:
            y -= 1
            sol += "Y"
        else:
            if sol[0] == "R":
                r -=1
                sol += "R"
            else:
                y -=1
                sol +="Y"
    if len(sol) > 1 and sol[0] == sol[len(sol) - 1] and sol != "IMPOSSIBLE":
        sol = "IMPOSSIBLE"
    elif sol != "IMPOSSIBLE":
        if o != 0:
            ind = sol.index("B")
            sol = sol[:ind] + "B" + ("OB" * o) + sol[ind+1:]
        if g != 0:
            ind = sol.index("R")
            sol = sol[:ind] + "R" + ("GR" * g) + sol[ind+1:]
        if v != 0:
            ind = sol.index("Y")
            sol = sol[:ind] + "Y" + ("VY" * v) + sol[ind+1:]


  #      for
    print (res + sol)
    i = i+ 1
    pos +=1
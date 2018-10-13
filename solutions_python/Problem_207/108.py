f = open('C:\\Users\\djspence\\Downloads\\B-large (1).in', 'r')

tries = int(f.readline())
    

for case in range(0, tries):
    vals = f.readline().strip().split(' ')
    n = int(vals[0])
    r = int(vals[1])
    o = int(vals[2])
    y = int(vals[3])
    g = int(vals[4])
    b = int(vals[5])
    v = int(vals[6])
    
    
    appendingO = ""
    appendingG = ""
    appendingV = ""
    
    if o == b and r+y+g+v == 0:
        print("Case #" + str(case+1) + ": " + "OB"*o)
        continue
    if g == r and o+y+b+v == 0:
        print("Case #" + str(case+1) + ": " + "GR"*g)
        continue
    if v == y and r+b+g+o == 0:
        print("Case #" + str(case+1) + ": " + "VY"*v)
        continue
    
    
    if o > 0:
        if b <= o:
            print("Case #" + str(case+1)+": IMPOSSIBLE")
            continue
        appendingO = "OB"*o
        b = b - o
        n = n - 2*o
        o = 0
    if g > 0:
        if r <= g:
            print("Case #" + str(case+1)+": IMPOSSIBLE")
            continue
        appendingG = "GR"*g
        r = r - g
        n = n - 2*g
        g = 0
    if v > 0:
        if y <= v:
            print("Case #" + str(case+1)+": IMPOSSIBLE")
            continue
        appendingV = "VY"*v
        y = y - v
        n = n - 2*v
        v = 0
    
    most = max(r, y, b)
    if most*2 > n:
        print("Case #" + str(case+1)+": IMPOSSIBLE")
    else:
        if most == r:
            mostL = "R"
            if y>b:
                second = y
                third = b
                secondL = "Y"
                thirdL = "B"
            else:
                second = b
                third = y
                secondL = "B"
                thirdL = "Y"
        if most == y:
            mostL = "Y"
            if r>b:
                second = r
                third = b
                secondL = "R"
                thirdL = "B"
            else:
                second = b
                third = r
                secondL = "B"
                thirdL = "R"
        if most == b:
            mostL = "B"
            if y>r:
                second = y
                third = r
                secondL = "Y"
                thirdL = "R"
            else:
                second = r
                third = y
                secondL = "R"
                thirdL = "Y"
        out = [0 for i in range(0, n)]
        str1 = mostL*most+secondL*second+thirdL*third
        counter = 0
        counter1 = 0
        while counter < n:
            out[counter] = str1[counter1]
            counter = counter + 2
            counter1 = counter1 + 1
        counter = 1
        while counter < n:
            out[counter] = str1[counter1]
            counter = counter + 2
            counter1 = counter1 + 1
        final = ""
        oAdded = False
        gAdded = False
        vAdded = False
        for adding in out:
            final = final + adding
            if adding == "B" and oAdded == False:
                oAdded = True
                final = final + appendingO
            if adding == "R" and gAdded == False:
                gAdded = True
                final = final + appendingG
            if adding == "Y" and vAdded == False:
                vAdded = True
                final = final + appendingV
        print("Case #" + str(case+1)+": " + final)

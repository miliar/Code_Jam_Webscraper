fin = open("B-large.in","rt")
fout = open("OUTPUT.txt","wt")

t = fin.readline().rstrip('\n')
t = int(t)

for case in range(1,t+1):
    sout = "Case #"+str(case)+": "
    n = fin.readline().rstrip('\n')
    n = [int(x) for x in n.split(" ")]

    r = n[1]
    y = n[3]
    b = n[5]
    cob = n[2] #O
    cor = n[4] #G
    coy = n[6] #V
    n = n[0]

    fixr = "R"
    fixy = "Y"
    fixb = "B"

    if cob > 0:
        if n == cob+b:
            if cob == b: sout += "OB"*cob
            else: sout += "IMPOSSIBLE"
            print sout
            fout.write(sout+'\n')
            continue
        if cob >= b:
            sout += "IMPOSSIBLE"
            print sout
            fout.write(sout+'\n')
            continue
        b -= cob
        fixb = "BO"*cob + "B"
    
    if cor > 0:
        if n == cor+r:
            if cor == r: sout += "GR"*cor
            else: sout += "IMPOSSIBLE"
            print sout
            fout.write(sout+'\n')
            continue
        if cor >= r:
            sout += "IMPOSSIBLE"
            print sout
            fout.write(sout+'\n')
            continue
        r -= cor
        fixr = "RG"*cor + "R"

    if coy > 0:
        if n == coy+y:
            if coy == y: sout += "VY"*coy
            else: sout += "IMPOSSIBLE"
            print sout
            fout.write(sout+'\n')
            continue
        if coy >= y:
            sout += "IMPOSSIBLE"
            print sout
            fout.write(sout+'\n')
            continue
        y -= coy
        fixy = "YV"*coy + "Y"

    if y > r+b or r > y+b or b > r+y:
        sout += "IMPOSSIBLE"
        print sout
        fout.write(sout+'\n')
        continue
 
    ss = ""
    guard = 0
    if max(r,y,b) == r:
        ss += fixr
        fixr = "R"
        r -= 0.9
        guard = 0
    elif max(r,y,b) == y:
        ss += fixy
        fixy = "Y"
        guard = 1
        y -= 0.9
    else:
        ss += fixb
        fixb = "B"
        guard = 2
        b -= 0.9
        
    while r+y+b > 0.5:
        if guard == 0:
            if y>b:
                ss += fixy
                fixy = "Y"
                guard = 1
                y -= 1
            else:
                ss += fixb
                fixb = "B"
                guard = 2
                b -= 1
        elif guard == 1:
            if r>b:
                ss += fixr
                fixr = "R"
                guard = 0
                r -= 1
            else:
                ss += fixb
                fixb = "B"
                guard = 2
                b -= 1
        else:
            if y>r:
                ss += fixy
                fixy = "Y"
                guard = 1
                y -= 1
            else:
                ss += fixr
                fixr = "R"
                guard = 0
                r -= 1
    sout += ss
    
    print sout
    fout.write(sout+'\n')

fout.close()

























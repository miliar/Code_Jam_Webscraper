def compatible(a, b):
    if a in [0,1,5] and b in [0,1,5]:
        return False #red
    if a in [1,2,3] and b in [1,2,3]:
        return False #yellow
    if a in [3,4,5] and b in [3,4,5]:
        return False #blue
    return True
    
def solve(line):
    [N, R, O, Y, G, B, V] = line.split()
    [N, R, O, Y, G, B, V] = map(int, [N, R, O, Y, G, B, V])
    res = []
    colors = [R, O, Y, G, B, V]
    for i in range(0, N):
        [R, O, Y, G, B, V] = colors
        Rc = Y + G + B
        Oc = B
        Yc = R + B + V
        Gc = R
        Bc = R + O + Y
        Vc = Y
        cMin = N
        cL = [Rc, Oc, Yc, Gc, Bc, Vc]
        sel = -1
        for j in range(0,6):
            if colors[j] == 0:
                continue
            if i > 0 and not compatible(j, res[i-1]):
                continue
            if i == N-1 and not compatible(j, res[0]):
                continue
            c = cL[j]
            if i > 0 and compatible(j, res[0]):
                c+=0.5
            if c < cMin:
                sel = j
                cMin = c
                
        #print(colors)
        #print(cL)
        #print(sel)
        if sel == -1:
            return "IMPOSSIBLE"

        res.append(sel)
        colors[sel]-=1
    
    s = ""
    chars = ["R", "O", "Y", "G", "B", "V"]
    for c in res:
        s += chars[c]
        
    return s
            
    

with open("B-large.in", "r") as ifile, open("out.txt", "w") as ofile:
    lines = ifile.readlines()
    T = lines[0]
    for i in range(1, len(lines)):
        line = lines[i].strip()
        ofile.write("Case #{}: {}\n".format(i, solve(line)))
        
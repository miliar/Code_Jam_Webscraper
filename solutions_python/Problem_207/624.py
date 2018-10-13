def main():
    infile = open("B-small-attempt0 (1).in", "r")
    outfile = open("B-small-attempt0 (1).out", "w")
    T = int(infile.readline())
    for i in range(T):
        line = infile.readline().split(" ")
        N = int(line[0])
        R = int(line[1])
        O = int(line[2])
        Y = int(line[3])
        G = int(line[4])
        B = int(line[5])
        V = int(line[6])
        outfile.write("Case #"+str(i+1)+": "+placeUnicorns(N,R,O,Y,G,B,V)+"\n")
    infile.close()
    outfile.close()

def placeUnicorns(N,R,O,Y,G,B,V):
    print(N,R,O,Y,G,B,V)
    s = ""
    if(O == B and O+B == N):
        for i in range(N):
            if(i % 2 == 0):
                s += "O"
            else:
                s += "B"
        return s
    if(G == R and G+R == N):
        for i in range(N):
            if(i % 2 == 0):
                s += "G"
            else:
                s += "R"
        return s
    if(V == Y and V+Y == N):
        for i in range(N):
            if(i % 2 == 0):
                s += "V"
            else:
                s += "Y"
        return s
    if(O > 2*B or G > 2*R or V > 2*Y):
        return "IMPOSSIBLE"

    count = 0
    if(O > 0):
        s += "B"
        B -= 1
        count += 1
        while(O > 0):
            s+= "OB"
            O -= 1
            B -= 1
            count += 2
            if(B < 0):
                return "IMPOSSIBLE"
    if(G > 0):
        s += "R"
        R -= 1
        count += 1
        while(G > 0):
            s+= "GR"
            G -= 1
            R -= 1
            count += 2
            if(R < 0):
                return "IMPOSSIBLE"
    if(V > 0):
        s += "Y"
        Y -= 1
        count += 1
        while(O > 0):
            s+= "VY"
            V -= 1
            Y -= 1
            count += 2
            if(Y < 0):
                return "IMPOSSIBLE"
    if(s == ""):
        if(B == max(B, R, Y)):
            s += "B"
            B -= 1
        elif(R == max(B, R, Y)):
            s += "R"
            R -= 1
        else:
            s += "Y"
            Y -= 1
        count += 1
    while(count < N):
        if(s[len(s)-1] == "B"):
            if(R > Y or (R == Y and s[0] == "R")):
                s += "R"
                R -= 1
            else:
                s += "Y"
                Y -= 1
            count += 1
        if(count == N):
            break
        if(s[len(s)-1] == "R"):
            if(B > Y or (B == Y and s[0] == "B")):
                s+= "B"
                B -=1
            else:
                s += "Y"
                Y -=1
            count += 1
        if(count == N):
            break
        if(s[len(s)-1] == "Y"):
            if(B > R or (B == R and s[0] == "B")):
                s += "B"
                B -= 1
            else:
                s += "R"
                R -=1
            count += 1
    if(s[0] == s[len(s)-1] or R < 0 or Y < 0 or B < 0):
        return "IMPOSSIBLE"
    return s

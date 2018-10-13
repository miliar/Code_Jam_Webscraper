from pprint import pprint

def verify(line, N, R, O, Y, G, B, V):
    if (line != "IMPOSSIBLE"):
        if (R != line.count("R") or \
            O != line.count("O") or \
            Y != line.count("Y") or \
            G != line.count("G") or \
            B != line.count("B") or \
            V != line.count("V")):
            print ("problem: ", N, R, O, Y, G, B, V);
            print(line);
            
def solve(N, R, O, Y, G, B, V):
    #print ("N R O Y G B V");
    #print (N, R, O, Y, G, B, V);
    if O>0:
        if (B==O and N==B+O):
            line = "BO" * int(N/2);
            fout.write(line + "\n");
            return line;
        if (B < O):
            fout.write("IMPOSSIBLE\n");
            return "IMPOSSIBLE";
    if G>0:
        if (R==G and N==R+G):
            line = "RG" * int(N/2);
            fout.write(line + "\n");
            return line;
        if (R < G):
            fout.write("IMPOSSIBLE\n");
            return "IMPOSSIBLE";
    if V>0:
        if (Y==V and N==Y+V):
            line = "YV" * int(N/2);
            fout.write(line + "\n");
            return line;
        if (Y < V):
            fout.write("IMPOSSIBLE\n");
            return "IMPOSSIBLE";
    BOB = "B";
    RGR = "R"
    YVY = "Y"
    if O>0:
        for i in range(O):
            BOB += "OB";
        B -= O;
    if G>0:
        for i in range(G):
            RGR += "GR";
        R -= G;
    if V>0:
        for i in range(V):
            YVY += "VY";
        Y -= V;
    reds = [];
    for i in range(R):
        if i==0:
            reds.append(RGR);
            continue;
        reds.append("R");
    yellows = [];
    for i in range(Y):
        if i ==0:
            yellows.append(YVY);
            continue;
        yellows.append("Y");
    blues = [];
    for i in range(B):
        if i==0:
            blues.append(BOB);
            continue;
        blues.append("B");
    line = "";
    l = [reds, yellows, blues];
    l.sort(key=len, reverse=True);
    #pprint(l);
    while (len(l[0]) + len(l[1]) + len(l[2]) > 0):
        if (len(l[0]) == len(l[1]) and len(l[1]) == len(l[2])):
            line += l[0].pop() + l[1].pop() + l[2].pop();
            continue;
        if (len(l[1])==-0):
            fout.write("IMPOSSIBLE\n");
            return "IMPOSSIBLE";
        line += l[0].pop() + l[1].pop();
        if (len(l[1]) < len(l[2])):
            l[1], l[2] = l[2], l[1];
        #print(line)
        #pprint(l);
    if (line[0] == line[-1]):
        fout.write("IMPOSSIBLE\n");
        return "IMPOSSIBLE";
    fout.write(line + "\n");
    return line;

lines = open("c:\codejam\B-small-attempt2.in").readlines()
fout = open("c:\codejam\B-small-attempt2.out", "w");
T = int(lines[0])
for tc in range(1,T+1):
    line = [int(x) for x in lines[tc].split()];
    N, R, O, Y, G, B, V = (line[0], line[1], line[2], line[3], line[4], line[5], line[6])
    fout.write("Case #" + str(tc) + ": ");
    print("Case #" + str(tc));
    line = solve(N, R, O, Y, G, B, V);
    verify(line, N, R, O, Y, G, B, V);
fout.close()

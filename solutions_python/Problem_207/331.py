t = int(input())

for c in range(t):
    N, R, O, Y, G, B, V = [int(item) for item in input().split()]
    output = ""
    if G > R or V > Y or O > B:
        print("Case #%d: IMPOSSIBLE" % (c + 1))
        continue
    if O:
        output += O * "BO" + "B"
        B -= O + 1
        O = 0

    if G:
        output += G * "RG" + "R"
        R -= G + 1
        G = 0

    if V:
        output += V * "YV" + "Y"
        Y -= V + 1
        V = 0

    if sum([R, Y, B]) <= 0:
        if output[0] == output[-1]:
            color = output[-1]
            if color == "R":
                R += 1
            elif color == "Y":
                Y += 1
            else:
                B += 1
            output = output[:-1]

    if output:
        last = output[-1]
    else:
        last = "R"
    while sum([R, Y, B]) > 0:
        if last == "R":
            if Y > B or (Y == B and output and output[0] == "Y"):
                last = "Y"
                output += "Y"
                Y -= 1
            else:
                last = "B"
                output += "B"
                B -= 1
        elif last == "Y":
            if R > B or (R == B and output[0] == "R"):
                last = "R"
                output += "R"
                R -= 1
            else:
                last = "B"
                output += "B"
                B -= 1
        else:
            if Y > R or (Y == R and output[0] == "Y"):
                last = "Y"
                output += "Y"
                Y -= 1
            else:
                last = "R"
                output += "R"
                R -= 1
    if R < 0 or Y < 0 or B < 0 or output[0] == output[-1]:
        print("Case #%d: IMPOSSIBLE" % (c + 1))
    else:
        print("Case #%d: %s" % (c + 1, output))

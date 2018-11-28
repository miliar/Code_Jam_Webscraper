f = open('B-small-attempt0.in', 'r')
o = open('B-small-attempt0.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    horses = f.readline().strip().split()
    N = int(horses[0])
    R = int(horses[1])
    O = int(horses[2])
    Y = int(horses[3])
    G = int(horses[4])
    B = int(horses[5])
    V = int(horses[6])
    O_block = ""
    G_block = ""
    V_block = ""
    failed = False
    while (not O == G == V == 0) and (not failed):
        if O > 0:
            while O > 0 and not failed:
                if B > 0:
                    O_block += "BO"
                    O -= 1
                    B -= 1
                    N -= 2
                else:
                    failed = True
            if N == 0:
                break
            elif B == 0:
                failed = True
            else:
                O_block += "B"
                B -= 1
                N -= 1
        if G > 0:
            while G > 0 and not failed:
                if R > 0:
                    G_block += "RG"
                    R -= 1
                    G -= 1
                    N -= 2
                else:
                    failed = True
            if N == 0:
                break
            elif R == 0:
                failed = True
            else:
                G_block += "R"
                R -= 1
                N -= 1
        if V > 0:
            while V > 0 and not failed:
                if Y > 0:
                    V_block += "YV"
                    Y -= 1
                    V -= 1
                    N -= 2
                else:
                    failed = True
            if N == 0:
                break
            elif Y == 0:
                failed = True
            else:
                V_block += "Y"
                Y -= 1
                N -= 1
    one_color_block = ""
    while (N > 0) and (not failed):
        if R >= B and R >= Y:
            one_color_block += "R"
            R -= 1
            N -= 1
            while R > 0 and not failed:
                if B == Y == 0:
                    failed = True
                elif B >= Y:
                    one_color_block += "BR"
                    B -= 1
                    R -= 1
                    N -= 2
                else:
                    one_color_block += "YR"
                    Y -= 1
                    R -= 1
                    N -= 2
        elif B >= R and B >= Y:
            one_color_block += "B"
            B -= 1
            N -= 1
            while B > 0 and not failed:
                if R == Y == 0:
                    failed = True
                elif R >= Y:
                    one_color_block += "RB"
                    B -= 1
                    R -= 1
                    N -= 2
                else:
                    one_color_block += "YB"
                    Y -= 1
                    B -= 1
                    N -= 2
        else:
            one_color_block += "Y"
            Y -= 1
            N -= 1
            while Y > 0 and not failed:
                if R == B == 0:
                    failed = True
                elif R >= B:
                    one_color_block += "RY"
                    Y -= 1
                    R -= 1
                    N -= 2
                else:
                    one_color_block += "BY"
                    Y -= 1
                    B -= 1
                    N -= 2
    result = ""
    if not failed:
        if one_color_block == "":
            result = O_block + G_block + V_block
        else:
            if not one_color_block[0] == "R":
                result = G_block + one_color_block
                if not one_color_block[-1] == "B":
                    result += O_block + V_block
                else:
                    result += V_block + O_block
            else:
                result = O_block + one_color_block
                if not one_color_block[-1] == Y:
                    result += V_block + G_block
                else:
                    result += G_block + V_block
    if len(result) > 0 and result[0] == result[-1]:
        failed = True
    if failed:
        result = "IMPOSSIBLE"
    s = "Case #%d: %s\n" % (t+1, result)
    o.write(s)
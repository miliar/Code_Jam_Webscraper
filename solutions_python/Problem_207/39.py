T = int(input())



def yup(R, Y, B):
    N = R + Y + B
    result = ""
    Y_ = 'Y'
    R_ = 'R'
    B_ = 'B'
    if Y <= N/2 and R <= N/2 and B <= N/2:
        if Y >= R and Y >= B:
            pass
        elif R >= Y and R >= B:
            Y, R = R, Y
            Y_, R_, = R_, Y_
        else:
            Y, B = B, Y
            Y_, B_, = B_, Y_
        fusions = R+B-Y
        for _ in range(fusions):
            result += Y_ + R_ + B_
        for _ in range(R-fusions):
            result += Y_ + R_
        for _ in range(B-fusions):
            result += Y_ + B_
        return result
    else:
        return "IMPOSSIBLE"
        # Y is in majority and R+B >= Y


def algo(N, R, O, Y, G, B, V):
    result = ""

    if Y <= N/2 and R <= N/2 and B <= N/2 and (O < B or B == 0) and (G < R or R == 0) and (V < Y or Y == 0):
        r = yup(R-G, Y-V, B-O)

        if r == "IMPOSSIBLE":
            return "IMPOSSIBLE"

        for i in range(len(r)):
            if r[i] == 'B' and O != 0:
                plo = "BO"*O
                r = r[0:i] + plo + 'B' + r[i+1:]
                break

        for i in range(len(r)):
            if r[i] == 'R' and G != 0:
                plo = "RG"*G
                r = r[0:i] + plo + 'R' + r[i+1:]
                break


        for i in range(len(r)):
            if r[i] == 'Y' and V != 0:
                plo = "YV"*V
                r = r[0:i] + plo + 'Y' + r[i+1:]
                break
        return r
    elif O == B and O + B == N:
         return "OB"*(N//2)
    elif G == R and G + R == N:
         return "GR"*(N//2)
    elif Y == V and Y + V == N:
         return "YV"*(N//2)
    else:
        return "IMPOSSIBLE"






for i in range(T):
    N, R, O, Y, G, B, V = [int(x) for x in input().split(' ')]
    print("Case #%d: %s" % (i+1, algo(N,R,O,Y,G,B,V)))

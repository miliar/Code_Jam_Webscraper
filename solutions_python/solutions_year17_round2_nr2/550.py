import sys

T = int(sys.stdin.readline().strip())

IMP = "IMPOSSIBLE"

def solve(N, R, O, Y, G, B, V):
    half = N//2

    if R > half:
        return IMP

    if O > half:
        return IMP

    if Y > half:
        return IMP

    if G > half:
        return IMP

    if B > half:
        return IMP

    if V > half:
        return IMP

    reds = V+R+O
    yellows = O+Y+G
    blues = G+B+V

    if reds > half:
        return IMP

    if yellows > half:
        return IMP

    if blues > half:
        return IMP

    if R < G or Y < V or B < O:
        return IMP

    curr = ""
    if R > 0 or Y > 0 or B > 0:
        if R >= Y and R >= B:
            curr = "R"
            R -= 1
        elif Y >= R and Y >= B:
            curr = "Y"
            Y -= 1
        else:
            curr = "B"
            B -= 1
    else:
        return IMP

    string = [curr]
    first = curr
    count = 1
    while count < N:
        #print(count, string)
        if curr == "R":
            if G > 0:
                curr = "G"
                G -= 1
            elif Y > 0 or B > 0:
                if Y == B:
                    if first == "Y":
                        #string.append("Y")
                        #count += 1
                        #Y -= 1
                        curr = "Y"
                        Y -= 1
                    else:
                        #string.append("B")
                        #count += 1
                        #B -= 1
                        curr = "B"
                        B -= 1
                elif Y > B:
                    curr = "Y"
                    Y -= 1
                else:
                    curr = "B"
                    B -= 1
            else:
                return IMP

        elif curr == "G":
            if R > 0:
                curr = "R"
                R -= 1
            else:
                return IMP

        elif curr == "Y":
            if V > 0:
                curr = "V"
                V -= 1
            elif B > 0 or R > 0:
                if B == R:
                    if first == "B":
                        #string.append("B")
                        #count += 1
                        #B -= 1
                        curr = "B"
                        B -= 1
                    else:
                        #string.append("R")
                        #count += 1
                        #R -= 1
                        curr = "R"
                        R -= 1
                elif B > R:
                    curr = "B"
                    B -= 1
                else:
                    curr = "R"
                    R -= 1
            else:
                return IMP

        elif curr == "V":
            if Y > 0:
                curr = "Y"
                Y -= 1
            else:
                return IMP

        elif curr == "B":
            if O > 0:
                curr = "O"
                O -= 1
            elif R > 0 or Y > 0:
                if R == Y:
                    if first == "R":
                        #string.append("R")
                        #count += 1
                        #R -= 1
                        curr = "R"
                        R -= 1
                    else:
                        #string.append("Y")
                        #count += 1
                        #Y -= 1
                        curr = "Y"
                        Y -= 1
                elif R > Y:
                    curr = "R"
                    R -= 1
                else:
                    curr = "Y"
                    Y -= 1
            else:
                return IMP

        else:
            if B > 0:
                curr = "B"
                B -= 1
            else:
                return IMP

        string.append(curr)
        count += 1

    #print(count, string)

    if curr in {"R", "O", "V"}:
        if first in {"R", "O", "V"}:
            return IMP

    if curr in {"Y", "G", "O"}:
        if first in {"Y", "G", "O"}:
            return IMP

    if curr in {"B", "G", "V"}:
        if first in {"B", "G", "V"}:
            return IMP

    return "".join(string)

for t in range(T):
    N, R, O, Y, G, B, V = [int(i) for i in sys.stdin.readline().split()]
    answer = solve(N, R, O, Y, G, B, V)
    print("Case #{}: {}".format(t+1, answer))


T = int(input())
for tid in range(T):
    (N, R, O, Y, G, B, V) = map(int, input().strip().split())
    if R + G == N:
        if R != G:
            print("Case #{}: IMPOSSIBLE".format(tid + 1))
        else:
            print("Case #{}: {}".format(tid + 1, "RG" * R))
    elif B + O == N:
        if B != O:
            print("Case #{}: IMPOSSIBLE".format(tid + 1))
        else:
            print("Case #{}: {}".format(tid + 1, "BO" * B))
    elif Y + V == N:
        if B != O:
            print("Case #{}: IMPOSSIBLE".format(tid + 1))
        else:
            print("Case #{}: {}".format(tid + 1, "YV" * Y))
    else:
        if R < G or B < O or Y < V:
            print("Case #{}: IMPOSSIBLE".format(tid + 1))
        else:
            RG = "RG" * G + "R"
            R -= G
            BO = "BO" * O + "B"
            B -= O
            YV = "YV" * V + "Y"
            Y -= V
            if max(R, B, Y) * 2 <= R + B + Y:
                if R == max(R, B, Y):
                    share = B + Y - R
                    R -= share
                    B -= share
                    Y -= share
                    result = "RBY" * share + "RB" * B + "RY" * Y
                elif B == max(R, B, Y):
                    share = Y + R - B
                    R -= share
                    B -= share
                    Y -= share
                    result = "BYR" * share + "BY" * Y + "BR" * R
                else:
                    share = R + B - Y
                    R -= share
                    B -= share
                    Y -= share
                    result = "YRB" * share + "YR" * R + "YB" * B

                result = result.replace("R", RG, 1)
                result = result.replace("B", BO, 1)
                result = result.replace("Y", YV, 1)
                print("Case #{}: {}".format(tid + 1, result))
            else:
                print("Case #{}: IMPOSSIBLE".format(tid + 1))
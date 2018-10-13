# 2^{S - K + 1} patterns to flip since flipping on the same spot will end up being the same.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    Nstr, Rstr, Ostr, Ystr, Gstr, Bstr, Vstr = input().split()  # read a list of integers, 2 in this case
    N = int(Nstr)
    R = int(Rstr)
    O = int(Ostr)
    Y = int(Ystr)
    G = int(Gstr)
    B = int(Bstr)
    V = int(Vstr)
    max_color_num = max(R, Y, B)
    if R + Y < B or R + B < Y or Y + B < R:
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))
        continue

    output = []
    RYB = [["R", R], ["Y", Y], ["B", B]]
    first = ""
    prev = ""
    for j in range(N):
        RYB_sorted = sorted(RYB, key=lambda x:(x[1], x[0]), reverse=True)
        #print(RYB_sorted)
        """
        1. not a prev
        2. use the frequent one
        3. use the not first char one
        """
        if prev != RYB_sorted[0][0]:
            k = 0
        else:
            if RYB_sorted[1][0] == first:
                k = 1
            else:
                k = 2
        output.append(RYB_sorted[k][0])
        prev = RYB_sorted[k][0]
        if j == 0:
            first = RYB_sorted[k][0]
        RYB_sorted[k][1] -= 1
        #if (R > 0) and (not prev == "R"):
        #    output[j] = "R"
        #    prev = "R"
        #    R -= 1
        #    continue
        #if Y > 0 and prev != "Y":
        #    output[j] = "Y"
        #    prev ="Y"
        #    Y -= 1
        #    continue
        #if B > 0 and prev != "B":
        #    output[j] = "B"
        #    prev = "B"
        #    B -= 1
        #    continue
 
    if N > 1 and output[-1] == output[0]:
        temp = output[-2]
        output[-2] = output[-1]
        output[-1] = temp
    #print(output)
    #for j in range(N):
    #    prev = output[j-1]
    #    if j == N-1:
    #        nex = output[0]
    #    else:
    #        nex = output[j+1]
    #    if prev
    print("Case #{}: {}".format(i, "".join(output)))
                

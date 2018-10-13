# for small case O = G = V = 0
filename = input()
f = open(filename + ".in")
o = open(filename + ".out", "w")
T = int(f.readline())

for t in range(1, T + 1):
    N, R, O, Y, G, B, V = list(map(int, f.readline().split()))
    order = []
    half = int(N / 2)
    group_red  = R + O + V
    group_blue = B + G + V
    group_yellow = Y + O + G
    if group_red > half or group_blue > half or group_yellow > half:
        print("Case #" + str(t) + ": IMPOSSIBLE")
        o.write("Case #" + str(t) + ": IMPOSSIBLE\n")
        continue
    pre = ""
    while group_red + group_blue + group_yellow > 0:
        m = max(group_red, group_red, group_yellow)
        if pre == "R":
            m = max(group_blue, group_yellow)
        elif pre == "B":
            m = max(group_red, group_yellow)
        elif pre == "Y":
            m = max(group_red, group_blue)
        
        if B == 1 and pre != "" and order[0] == "B" and pre != "B":
            order.append("B")
            B -= 1
            pre = "B"
            continue
        if Y == 1 and pre != "" and order[0] == "Y" and pre != "Y":
            order.append("Y")
            Y -= 1
            pre = "Y"
            continue
        
        if m == group_red and pre != "R":
            order.append("R")
            R -= 1
            pre = "R"
        elif m == group_blue and pre != "B":
            order.append("B")
            B -= 1
            pre = "B"
        else:
            order.append("Y")
            Y -= 1
            pre = "Y"
        # update
        group_red  = R + O + V
        group_blue = B + G + V
        group_yellow = Y + O + G
    print("Case #" + str(t) + ": " + "".join(order))
    o.write("Case #" + str(t) + ": " + "".join(order) + "\n")
f.close()
o.close()

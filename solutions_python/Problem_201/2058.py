def stalls (N, K):
    st = list()
    st.append("O")
    for i in range(N):
        st.append(".")
    st.append("O")
    maxim = 0
    minim = 0
    for i in range(K):

        maxim = -1
        minim = -1
        stall = 0
        for s in range(1, N + 1):
            if st[s] == "O" :
                continue
            l = left(st, s)
            r = right(st, s)
            mi = min(l, r)
            ma = max(l, r)
            if mi > minim or mi == minim and ma > maxim:
                stall = s
                minim = mi
                maxim = ma

        st[stall] = "O"
    return str(maxim) + " " + str(minim)

def left(l, position):
    for i in range(position, -1, -1):
        if l[i] == "O":
            return position - i - 1

def right(l, position):
    for i in range(position, len(l) + 2):
        if l[i] == "O":
            return i - position - 1


with open("E:\Python\CodeJam\C-small-1-attempt0.in", "r") as f:
    data = f.readlines()[1:]
f.close()
with open("E:\Python\CodeJam\C-small-1-attempt0.txt", "w") as w:
    for i in range(len(data)):
        inp = data[i].split(" ")
        w.write("Case #" + str(i + 1) + ": " + str(stalls(int(inp[0]), int(inp[1]))) + "\n")
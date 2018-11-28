f = open("e.in")
fout = open("e.out", "w")

input_str = f.readline()
t = int(input_str)

for case in range(1, t + 1):
    input_str = f.readline()
    splitted = input_str.split()
    pline = splitted[0]
    arr = [False if ch == '-' else True for ch in pline]
    w = int(splitted[1])
    l = len(arr)

    out = 0
    it = 0
    while it < l - w:
        if not arr[it]:
            out += 1
            for jt in range(it, it + w):
                arr[jt] = not arr[jt]
        it += 1

    if not arr[it]:
        out += 1
    result = True
    for jt in range(it, l - 1):
        if arr[jt] != arr[jt + 1]:
            fout.write("Case #%d: IMPOSSIBLE\n" % case)
            result = False
            break

    if result:
        fout.write("Case #%d: %d\n" % (case, out))

f.close()
fout.close()

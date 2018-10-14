f = open("C:\\Users\\TocarIP\\Google Drive\\Downloads\\A-large.in")
lines = f.readlines()
numcases = int(lines[0])
i = 1
while i <= numcases:
    yyy,xxx = lines[i].split(" ")
    ln = int(xxx)
    seq = []
    for c in yyy:
        if c == '-':
            seq.append(True)
        else:
            seq.append(False)
    res_int = 0
    for j in range(len(seq) - ln + 1):
        if seq[j]:
            res_int += 1
            for q in range(ln):
                seq[j+q] = not seq[j+q]
    res = "Case #" + str(i) + ": "
    flag = True
    for q in seq:
        if q:
            res += "IMPOSSIBLE"
            flag = False
            break
    if flag:
        res += str(res_int)
    print (res)
    i = i+ 1
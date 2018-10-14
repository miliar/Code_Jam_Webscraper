T = int(raw_input())
for t in range(T):
    R, C = map(int, raw_input().strip().split(" "))
    letts = []
    for i in range(R):
        letts.append([x for x in raw_input().strip()])
    for i in range(R):
        index = C
        for j, char in enumerate(letts[i]):
            if char!="?":
                first = char
                index = j
                break
        if index!=C:
            letts[i][:index] = [first]*index
            for j in range(index,C):
                if letts[i][j]=="?":
                    letts[i][j] = first
                else:
                    first =letts[i][j]
        index = 0
    if letts[0][0]=="?":
        while letts[index][0]=="?":
            index += 1
        letts[:index] = [letts[index]]*index
    for j in range(index,R):
        if letts[j][0]=="?":
            letts[j] = letts[j-1]
    print "Case #%d:" % (t+1)
    for chars in letts:
        print "".join(chars)

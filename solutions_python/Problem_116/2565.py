inlist = open("file.in","r").readlines()
cases = eval(inlist.pop(0))

for i in range(len(inlist)): inlist[i] = inlist[i].strip("\n")
inlist = [val for val in inlist if val != '']

table = []
for i in range(cases):
	table.append(inlist[i*4:i*4+4])
	for j in range(4):
		table[-1][j] = list(table[-1][j])

for i in range(cases):
    case = table[i]
    completed = True
    done = False

    #horizontal

    for y in range(4):
        if not done:
            s = case[y][0]
            if s == "T": s = case[y][1]
            if s == ".": completed = False
            elif case[y].count(s) == 4 - case[y].count("T"):
                print("Case #"+str(i+1)+": "+s+" won")
                done = True

	#vertical

    for x in range(4):
        if not done:
            set = [case[val][x] for val in range(4)]
            s = case[0][x]
            if s == "T": s = case[1][x]
            if s == ".": completed = False
            elif set.count(s) == 4 - set.count("T"):
                print("Case #"+str(i+1)+": "+s+" won")
                done = True

    #diagonal
    if not done:
        set1 = [case[x][x] for x in range(4)]
        s = set1[0]
        if s == "T": s = set1[1]
        if s == ".": completed = False
        elif set1.count(s) == 4 - set1.count("T"):
            print("Case #"+str(i+1)+": "+s+" won")
            done = True
    if not done:
        set2 = [case[x][3-x] for x in range(4)]
        s = set2[0]
        if s == "T": s = set2[1]
        if s == ".": completed = False
        elif set2.count(s) == 4 - set2.count("T"):
            print("Case #"+str(i+1)+": "+s+" won")
            done = True

    #still not done
    if not done:
        if completed: print("Case #"+str(i+1)+": Draw")
        else: print("Case #"+str(i+1)+": Game has not completed")










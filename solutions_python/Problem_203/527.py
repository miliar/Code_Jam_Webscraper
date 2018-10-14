inp = open("cake.in", 'r')
opt = open("cake.out", 'w')

T = None
Rs = []
Cs = []
grids = []
N = 0
num = True
n = 0
for line in inp:
    if T is None:
        T = int(line)
    else:
        if num:
            l = line.split(" ")
            Rs.append(int(l[0]))
            Cs.append(int(l[1]))
            grids.append([])
            num = False
        else:
            grids[N].append(list(line[:-1]))
            n += 1
            if n == Rs[N]:
                num = True
                N += 1
                n = 0



# go through each ?, find all of the possible letters it could be:
#   go through all letters, look at rectangle formed by the ? and the letter
#   if there are only ?'s in the rectangle, it could be that letter
# assign all ?'s with only 1 possiblity
# go through all possibliities for all ?'s until a valid combination is found
# invalid combination is one where assigning a letter causes a rectangle that contains a different letter

# BETTER OPTION:
# set each ? to the letter closest below it. If there is none, go up.
# The only remaining ?'s will be in empty columns.
# Now set each remaining ? to the letter to its left. If there is none, go right.

for x in range(T):
    grid = grids[x]
    R = Rs[x]
    C = Cs[x]
    for r in range(R):
        for i in range(len(grid[r])):
            if grid[r][i] == '?':
                changed = False
                for d in range(r+1,R):
                    e = grid[d][i]
                    if e != '?':
                        grid[r][i] = e
                        changed = True
                        break
                if not changed:
                    for u in range(r):
                        e = grid[u][i]
                        if e != '?':
                            grid[r][i] = e
    # now there should only be ?'s in empty columns
    # could make the search for said empty columns faster by saving those unchanged previously
    for r in range(R):
        for i in range(len(grid[r])):
            if grid[r][i] == '?':
                changed = False
                for ri in range(i+1,C):
                    e = grid[r][ri]
                    if e != '?':
                        grid[r][i] = e
                        changed = True
                        break
                if not changed:
                    for l in range(i):
                        e = grid[r][l]
                        if e != '?':
                            grid[r][i] = e
    # could maybe make this faster by also setting the cells below and above a cell when we assign it in this step
    # now convert lists to strings and output them
    opt.write("Case #" + str(x+1) + ":\n")
    for r in range(R):
        new = ""
        for c in grid[r]:
            new += c
        opt.write(new + "\n")

opt.close()

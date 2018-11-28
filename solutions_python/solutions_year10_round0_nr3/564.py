
common_name = "C-small-attempt0"
infile_name = common_name + ".in"
outfile_name = common_name + ".out"

number = []     #running times
capacity = []   #capacity
group_size = [] #group size
group = []      #group

fin = open(infile_name, "r")
nin = int(fin.readline())

for i in range(nin):
    astr = fin.readline()
    a, b, c = str(astr).split()  # R, k, n / run times, capacity, group number
    number.append(int(a))
    capacity.append(int(b))
    group_size.append(int(c))
    group.append([])

    astr = fin.readline()
    alist = str(astr).split()
    for j in range(group_size[i]) :
        group[i].append(int(alist[j]))
fin.close()

#print number, capacity, group_size, group

fout = open(outfile_name, "w")
for i in range(nin):
    res = 0
    pos = 0
    #print capacity[i], group[i]

    for j in range(number[i]):
        now = 0
        remember = pos  # do not cycle more than one(line is limited for riding)
        while(True):
            #print now, pos
            if capacity[i] < now + group[i][pos]:
                break
            now += + group[i][pos]
            pos += 1
            if pos >= group_size[i]:
                pos = 0
            if pos == remember:
                break
        res += now
    astr = "Case #%d: %d\n" %(i + 1, res)
    #print astr
    fout.write(astr)
fout.close()
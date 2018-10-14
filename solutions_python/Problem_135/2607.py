infile = open("A-small-attempt0.in", 'rb')
outfile = open("A-small-attempt0.out", 'w')
lines = [x.lstrip().rstrip() for x in infile.readlines()]
probs = int(lines[0])

def get_board(lines, p, first):
    if first:
        b = lines[1+(p-1)*10+1:1+(p-1)*10+1+4]
    else:
        b = lines[1+(p-1)*10+6:1+(p-1)*10+10]
    b1 = []
    for l in b:
        b1.append([int(x) for x in l.split()])
    return b1
        
    

def get_answer(lines, p, first):
    if first:
        return int(lines[1+(p-1)*10])-1
    else:
        return int(lines[1+(p-1)*10+5])-1

for p in range(1, probs+1):
    outfile.write("Case #"+str(p)+": ")
    b1 = get_board(lines, p, True)
    b2 = get_board(lines, p, False)
    a1 = get_answer(lines, p, True)
    a2 = get_answer(lines, p, False)
    line1 = b1[a1]
    line2 = b2[a2]
    common = [x for x in line1 if x in line2]
    if (len(common)==1):
        outfile.write(str(common[0]))
    if (len(common)==0):
        outfile.write("Volunteer cheated!")
    if (len(common)>1):
        outfile.write("Bad magician!")
    outfile.write("\n")

outfile.close()

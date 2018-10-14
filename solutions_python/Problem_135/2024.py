infile = "A-small-attempt0.in.txt" 
outfile = "magic_small.out"

file = open(infile, 'rU')
content = file.read()
content = content.splitlines()

T = int(content[0])
content.pop(0)
file.close()

result = []

for i in range(0, T):
    base = i * 10;
    ans1 = int(content[base]) - 1
    row1 = content[base + ans1 + 1].split()
    ans2 = int(content[base + 5]) - 1
    row2 = content[base + 6 + ans2].split();
    intersect = list(set(row1).intersection(set(row2)))
     
    s = "Case #" + str(i + 1) + ": "
    if(len(intersect) > 1):
        s += "Bad magician!\n"
    elif(len(intersect) == 0):
        s += "Volunteer cheated!\n"
    else:
        s += intersect[0] + "\n"
    
    result.append(s)

file = open(outfile, 'w')
for l in result:
    file.write(l)

file.close()

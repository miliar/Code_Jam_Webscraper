inp = open('A-small-attempt0.in', 'r')
out = open('out.txt', 'w')

nTests = int(inp.readline())

for i in range(1, nTests+1):
    row = [None]*2
    pos = [None]*2

    for k in range(2) :
        row[k] = int(inp.readline())
    
        for j in range(1, 5):
            line = inp.readline()
            if j == row[k]:
                pos[k] = [int(l) for l in line.split()]

    com = set(pos[0]) & set(pos[1])
    coml = len(com)

    out.write("Case #" + str(i) + ": ")
    if coml == 1:
        out.write(str(com.pop()))
    elif coml == 0:
        out.write("Volunteer cheated!")
    else:
        out.write("Bad magician!")
    out.write("\n")


            

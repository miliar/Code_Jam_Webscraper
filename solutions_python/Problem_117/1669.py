
f = open('B-small-attempt0.in')
p = open('output.txt','w')

numCases = int(f.readline())

for l in range(1,int(numCases)+1):
    sizes = f.readline().split(' ')
    lines = []
    out = []

    for i in range(0,int(sizes[0])):
        out.append([])
        for j in range(0,int(sizes[1])):
            out[i].append(100)
    
    for i in range(1,int(sizes[0])+1):
        lines.append(f.readline().strip().split(' '))
        m = int(max(lines[i-1]))
        for j in range(1,int(sizes[1])+1):
            lines[i-1][j-1] = int(lines[i-1][j-1])
            out[i-1][j-1] = m
                
    for j in range(0,int(sizes[1])):
        min1 = 00
        for i in range(0,int(sizes[0])):
            if int(lines[i][j]) > min1:
                min1 = int(lines[i][j])
        for i in range(0,int(sizes[0])):
            if out[i][j] > min1:
                out[i][j] = min1
                


    if lines == out:
        p.write("Case #" + str(l) + ": YES\n")
    else:
        p.write("Case #" + str(l) + ": NO\n")

f.close()
p.close()

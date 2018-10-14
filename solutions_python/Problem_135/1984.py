infile = open('A-small-attempt2.in','r')
cases = int(infile.readline().strip())
outfile = open('magic.out.txt','w')

for case in range(1,cases+1):
    resp1 = int(infile.readline().strip())
    mynums = ''
    for row in range(4):
        nums = infile.readline().strip()
        if row+1 == resp1:
            mynums = nums.split()
    for x in mynums:
        x = int(x)
    resp2 = int(infile.readline().strip())
    mynewnums = ''
    for row in range(4):
        nums = infile.readline().strip()
        if row+1 == resp2:
            mynewnums = nums.split()
    for x in mynums:
        x = int(x)
    possible = []
    for x in mynums:
        if x in mynewnums:
            possible.append(x)
    if len(possible) == 0:
        outfile.write('Case #'+str(case)+': Volunteer cheated!\n')
    elif len(possible) == 1:
        outfile.write('Case #'+str(case)+': '+str(possible[0])+'\n')
    else:
        outfile.write('Case #'+str(case)+': Bad magician!\n')
outfile.close()

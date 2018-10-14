infile = open('A-small-attempt0 (1).in','r')
outfile = open('1out.txt','w')
total = int(infile.readline())
for t in range(total):
    num = [0 for i in range(17)]
    row1 = int(infile.readline())
    row = ''
    for i in range(4):
        line =  infile.readline()
        if i==row1-1:
            row = line
    row = row.split(' ')
    for item in row:
        num[int(item)] += 1

    row2 = int(infile.readline())
    row = ''
    for i in range(4):
        line =  infile.readline()
        if i==row2-1:
            row = line
    row = row.split(' ')
    for item in row:
        num[int(item)] += 1

    ans = []
    for i in range(17):
        if num[i]==2:
            ans.append(i)
    l = len(ans)
    if l==0:
        outfile.write('Case #'+str(t+1)+': '+'Volunteer cheated!\n')
    elif l==1:
        outfile.write('Case #'+str(t+1)+': '+str(ans[0])+'\n')
    else:
        outfile.write('Case #'+str(t+1)+': '+'Bad magician!\n')
infile.close()
outfile.close()

with open('input') as infile:
    content = infile.readlines()
    for x in range(0, int(content[0])):
        ans1 = int(content[x*10+1])
        ans2 = int(content[x*10+6])
        grid1 = [content[x*10+2].rstrip('\n').split(' '),content[x*10+3].rstrip('\n').split(' '),content[x*10+4].rstrip('\n').split(' '),content[x*10+5].rstrip('\n').split(' ')]
        grid2 = [content[x*10+7].rstrip('\n').split(' '),content[x*10+8].rstrip('\n').split(' '),content[x*10+9].rstrip('\n').split(' '),content[x*10+10].rstrip('\n').split(' ')]
        output = set(grid1[ans1-1]) & set(grid2[ans2-1])
        print('Case #{0}: {1}'.format(str(x+1), str(output.pop()) if len(output) ==1 else 'Volunteer cheated!' if len(output) == 0 else 'Bad magician!'))
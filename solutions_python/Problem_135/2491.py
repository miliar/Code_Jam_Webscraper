def go():
    fin = open('codejamA.txt', 'r')
    numcases = int(fin.readline())
    for i in range(numcases):
        choice = int(fin.readline()) - 1
        for j in range(4):
            line = fin.readline()
            if j == choice:
                possibilities = {thing for thing in line.split()}
        newchoice = int(fin.readline()) - 1
        result = None
        for j in range(4):
            line = fin.readline()
            if j == newchoice:
                elems = {num for num in line.split() if num in possibilities}
                if len(elems) == 1:
                    result = 'Case #{}: {}'.format(i + 1, elems.pop())
                elif len(elems) > 1:
                    result = 'Case #{}: Bad magician!'.format(i + 1)
                else:
                    result = 'Case #{}: Volunteer cheated!'.format(i + 1)
        print(result)
        
go()
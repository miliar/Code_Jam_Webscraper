f = open('A-small-attempt0 (2).in', 'r')
g = open('output.txt', 'w')
n = int(f.readline())
for i in range (1, n+1):
    found = 0
    row1 = f.readline()
    ints1 = []
    ints2 = []
    line = 'Case #' + str(i) + ': '
    for x in range (0, 4):
        string = f.readline()
        if x == int(row1)-1:
            ints1 = string.split();
    row2 = f.readline()
    for x in range (0, 4):
        string = f.readline()
        if x == int(row2)-1:
            ints2 = string.split();
    matches = list(set(ints1) & set(ints2));
    if len(matches) == 0:
    	line = line + 'Volunteer cheated!\n'
    elif len(matches) == 1:
    	line = line + str(matches[0]) + '\n'
    else:
    	line = line + 'Bad magician!\n'
    g.write(line) 
f.close()
g.close()
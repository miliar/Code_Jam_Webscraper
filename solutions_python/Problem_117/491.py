'''
Created on Apr 13, 2013

@author: Sean Groathouse
'''

fin = open('B-large.in', 'r')
finput = fin.readlines()
fin.close()
it = iter(finput)
numbCases = (int)(it.next())
output = ""

for case in xrange(numbCases):
    answer = "YES"
    line = (it.next().rstrip().split())
    rows = (int)(line[0])
    columns = (int)(line[1])
    grid = list()
    for i in xrange(rows):
        row = (it.next().rstrip().split())
        for j in range(len(row)):
            row[j] = (int)(row[j])
        grid.append(row)
    
    for i in xrange(rows):
        for j in xrange(columns):
            rowWorks = True
            colWorks = True
            for x in xrange(rows):
                if grid[x][j] > grid[i][j]:
                    colWorks = False
            for y in xrange(columns):
                if grid[i][y] > grid[i][j]:
                    rowWorks = False
            if not (colWorks or rowWorks):
                answer = "NO"
    
    output += "Case #%d: %s\n" % (case+1, answer)
    
fout = open('large.txt', 'w')
fout.write(output)
fout.close()
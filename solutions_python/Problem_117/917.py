__author__ = 'israel.roth@gmail.com'

import datetime


def mow_result(n, m, desired_lawn_pattern):
    # local copy to try and cut...
    lawn = []
    for drow in desired_lawn_pattern:
        local = drow[:]
        lawn.append(local)

    # cut the grass along the rows to the maximum desired height in that row
    for row in lawn:
        max_desired_height = max(row)
        for i in range(0,len(row)):
            row[i] = max_desired_height     # grass starts at 100, so surely it is cut

    # cut the grass along the columns to the maximum desired height in that column

    for ci in range(0,m):
        desired_col = [desired_lawn_pattern[i][ci] for i in range(0,n)]
        max_desired_height = max(desired_col)
        for i in range (0,n):
            lawn[i][ci] = min(lawn[i][ci], max_desired_height)
            if lawn[i][ci] != desired_lawn_pattern[i][ci]:
                return "NO"

    # if all columns are ok, the whole lawn is ok
    return "YES"

# ok, get test cases...

testfile = open ('Lawnmower.in')
line = testfile.readline()
ntests = int(line)

outfile = open('Lawnmower.out', 'w')

print datetime.datetime.now()

for testnum in range(0,ntests):
    size = [int(i) for i in testfile.readline()[:-1].split()]
    n = size[0]
    m = size[1]

    lawn = []
    for ri in range(0,n):
        row = [int(i) for i in testfile.readline()[:-1].split()]
        lawn.append(row)

    result = mow_result(n, m, lawn)

    # sys.stdout.write(".")
    outfile.write ("Case #"+str(testnum+1)+": " + result + "\n")
    print ("Case #"+str(testnum+1)+": " + result)

print datetime.datetime.now()

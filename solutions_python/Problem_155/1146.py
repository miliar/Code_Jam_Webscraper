from sys import stdin

lines = int(stdin.readline())

for i in range(1, lines+1):
    line = stdin.readline()
    line = line.split(' ')

    res = 0
    standing = 0
    for j in range(int(line[0])+1):
        if standing < j:
            standing += 1
            res += 1
        standing += int(line[1][j])
    print "Case #{}: {}".format(i, res)

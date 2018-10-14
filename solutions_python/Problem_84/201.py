import fileinput

def solve(pic):
    for y, row in enumerate(pic):
        for x, tile in enumerate(row):
            if y == len(pic)-1 or x == len(row)-1:
                continue
            if tile==row[x+1]==pic[y+1][x]==pic[y+1][x+1]=='#':
                pic[y][x] = '/'
                pic[y][x+1] = '\\'
                pic[y+1][x] = '\\'
                pic[y+1][x+1] = '/'
    for row in pic:
        if '#' in row:
            yield 'Impossible'
            return
    for row in pic:
        yield ''.join(row)

readline = fileinput.input().readline
case_count = int(readline())
for case_no in range(case_count):
    rows, cols = [int(x) for x in readline().split()]
    pic = []
    for i in range(rows):
        pic.append(list(readline().strip()))
    answer = solve(pic)
    print "Case #%d:\n%s" % (case_no+1, '\n'.join(answer))

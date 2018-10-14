import math
f = open('B-large.in', 'r')
g = open('output3.txt', 'w')
cases = int(f.readline())
count = 0
for i in range (1, cases+1):
    N, M = [int(x) for x in f.readline().split()]
    garden = []
    for j in range (0, N):
        row = [int(n) for n in f.readline().split( )]
        garden.append(row)
    nums = sum(garden, [])
    while len(nums) > 0:
        spliced = False
        x, y = 0, 0
        smallest = min(nums)
        for k in range (0, len(garden)):
            row = garden[k]
            if smallest in row:
                if all(num == row[0] for num in row):
                    garden.remove(row)
                    nums = sum(garden, [])
                    spliced = True
                    break
        if not spliced:
            inverted = map(list, zip(*garden))
            for k in range (0, len(inverted)):
                column = inverted[k]
                if smallest in column:
                    if all(num == column[0] for num in column):
                        inverted.remove(column)
                        garden = map(list, zip(*inverted))
                        nums = sum(garden, [])
                        spliced = True
                        break    
            if not spliced:
                line = 'Case #' + str(i) + ': NO\n'
                g.write(line)
                break
    if len(nums) < 1:    
        line = 'Case #' + str(i) + ': YES\n'
        g.write(line)      
f.close()
g.close()
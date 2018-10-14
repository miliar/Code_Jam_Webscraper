'''
def check(grid):
	S = {}
	for i in grid:
		for j in i:
			if j in S:
				S[j].append((i,j))
			else:
				S[j] = [(i,j)]
    valid=True
    for letter in S:
        rows = [i[0] for i in S[letter]]
        columns = [i[1] for i in S[letter]]
        r1 = min(rows)
        r2 = max(rows)
        c1 = min(columns)
        c2 = max(columns)
        
    return valid
'''

def fix(grid):
    for row in grid:
        for s in row:
            if not s == '?':
                   break
        if not s == '?':
            for i in range(len(row)):
                if row[i]=='?':
                    row[i] = s
                else:
                    s = row[i]
    for i in range(len(grid)):
        if not grid[i][0]=='?':
            previous = list(grid[i])
            break
    for i in range(len(grid)):
        if grid[i][0]=='?':
            grid[i] = list(previous)
        else:
            previous = grid[i]

f = open('A-large.in')
N = int(f.readline())
for i in range(N):
    l = f.readline()
    R = int(l.split()[0])
    C = int(l.split()[1])
    grid = []
    for j in range(R):
        l = f.readline().strip()
        grid.append([s for s in l])
    fix(grid)
    print 'Case #%d:' % (i+1)
    for row in grid:
        print ''.join(row)
		
		
	
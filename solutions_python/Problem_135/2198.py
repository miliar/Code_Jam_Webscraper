import sys

file = open(sys.argv[1], 'rb')
outfile =open('out.txt', 'wb')
n = int(file.next())

for n_i in xrange(n):
    ans1 = int(file.next())
    grid = []
    for i in xrange(4):
        grid += [file.next().split()]
    set1 = set(grid[ans1-1])
    ans2 = int(file.next())
    grid = []
    for i in xrange(4):
        grid += [file.next().split()]
    set2 = set(grid[ans2-1])
    ans = set1.intersection(set2)
    
    if len(ans)==1:
        outans = ans.pop()
    elif len(ans)>1:
        outans ='Bad magician!'
    elif len(ans)==0:
        outans ='Volunteer cheated!'
    outfile.write('Case #%s: %s\n' %((n_i+1), outans))

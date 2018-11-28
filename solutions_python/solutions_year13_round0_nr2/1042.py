filename = 'B-large'

f = open(filename + '.in')

outfile = open(filename + '.out', 'w')


for case in xrange(int(f.readline())):
    print case
    r, c = map(int, f.readline().split())
    original = [[100]*c for i in xrange(r)]
    final = []
    for a in xrange(r):
        final.append(map( int, f.readline().split(' ')))
    
    for i in xrange(r):
        row = final[i]
        height = max(row)
        for j in xrange(c):
            original[i][j] = min(original[i][j], height)
    for i in xrange(c):
        height = max([final[row][i] for row in xrange(r)])
        for row in xrange(r):
            original[row][i] = min(original[row][i], height)
    
    # Compare
    done = False
    for i in xrange(r):
        for j in xrange(c):
            if original[i][j] != final[i][j]:
                outfile.write('Case #%d: NO\n' % (case+1,))
                done = True
                break
            
        if done:
            break
    if not done:
        outfile.write('Case #%d: YES\n' % (case+1,))
        
            


outfile.close()
f.close()

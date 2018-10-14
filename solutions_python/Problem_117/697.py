fin = open("B-small-attempt0.in")
fout = open("prob2.out", "w")

num_cases = int(fin.readline())

for case_number in xrange(num_cases):
    rows, cols = map(int, fin.readline().split())
    possible = True
    lawn = []
    for row in xrange(rows):
        lawn.append(fin.readline().split())

    for row in xrange(rows):
        if possible == False:
            break
        for col in xrange(cols):
            possible2 = False
            height = lawn[row][col]
            if all([grass <= height for grass in lawn[row]]):
                possible2 = True
            elif all([grass <= height for grass in [lawn[row2][col] for row2 in xrange(rows)]]):
                possible2 = True
            if possible2 == False:
                print row, col
                possible = False
                break

    print "Case #%d: %s\n" % (case_number+1, "YES" if possible else "NO")
    fout.write("Case #%d: %s\n" % (case_number+1, "YES" if possible else "NO"))
    
fout.close()


# read input and compute set intersections
solutions = []
with open('input') as file:
    T = int(file.readline()) # test cases
    for i in xrange(T):
        picked_rows = []
        for j in xrange(2):
            picked_row = int(file.readline())-1
            for k in xrange(4):
                line = file.readline()
                if k == picked_row:
                    picked_rows.append(set(line.split()))
        solutions.append(picked_rows[0].intersection(picked_rows[1]))

# output print solutions
for i, sol in enumerate(solutions):
    if len(sol) == 1:
        output = iter(sol).next()
    elif len(sol) == 0:
        output = "Volunteer cheated!"
    else:
        output = "Bad magician!"
    print "Case #%i: %s" % (i+1, output)

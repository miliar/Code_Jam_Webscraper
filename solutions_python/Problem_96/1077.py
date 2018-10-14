
def solvecase(n, surprises, limit, points):
    points.sort()
    print limit
    print surprises
    print points
    result = len(filter(lambda x: x+2 >= 3*limit, points))
    print filter(lambda x: x+2 >= 3*limit, points)
    points = filter(lambda x: x+2 < 3*limit, points)
    if surprises != 0:
        points = filter(lambda x: x != 0, points)
        points = points[-surprises:]
        print points
        result += len(filter(lambda x: x+4 >= 3*limit, points))
    return result
    
fin = open('B-large.in', 'r')
cases = int(fin.readline())

fout = open('out', 'w')
for i in range(cases):
    case = fin.readline()
    case = [int(x) for x in case.split()]
    points = case[3:]
    n, surprises, limit = case[:3]
    result = solvecase(n, surprises, limit, points)
    fout.write('Case #' + str(i+1) + ': ' + str(result) + '\n')
    print 'Case #' + str(i+1) + ': ' + str(result) + '\n',
    
fout.close()
fin.close()

 

import sys

fp = open('large.in', 'r')
out = open('output', 'w')

#fp = open('input', 'r')
#out = sys.stdout

cases = int(fp.readline())

for case in range(cases):
    existe = set()
    
    parms = [int(x) for x in fp.readline().split()]

    for x in range(parms[0]):
        row = fp.readline().strip()
        path = '/'
        for dir in row[1:].split('/'):
#            print path + dir
            existe.add(path + dir)
            path = path + dir + '/'
    
    result = 0
    for y in range(parms[1]):
        row = fp.readline().strip()
        path = '/'
        for dir in row[1:].split('/'):
#            print path + dir
            if path+dir not in existe:
                result += 1
                existe.add(path+dir)
            path = path + dir + '/'
    
    out.write('Case #' + str(case + 1) + ': ' + str(result) + '\n')
    case += 1

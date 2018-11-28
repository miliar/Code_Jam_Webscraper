def isrecycled(n, m):
    return (str(n) + str(n)).rfind(str(m)) >= 0 

def solvecase(a, b):
    count = 0
    for m in range(a, b+1):
        for n in range(a, m):
            if isrecycled(n, m):
                count += 1
    return count
            


fin = open('C-small-attempt0.in', 'r')
cases = int(fin.readline())

fout = open('out', 'w')
for i in range(cases):
    case = fin.readline()
    a, b = case.split()
    a = int(a)
    b = int(b)
    result = solvecase(a, b)
    fout.write('Case #' + str(i+1) + ': ' + str(result) + '\n')
    print 'Case #' + str(i+1) + ': ' + str(result) + '\n',
    
fout.close()
fin.close()

 

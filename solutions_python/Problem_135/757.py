

def solveA(file):
    data = ''
    resultTotal = []
    with open(file) as f:
        T = f.readline()
        T = int(T.strip())
        for index in xrange(T):
            A1 = f.readline()
            A1 = int(A1.strip())
            rows1 = [f.readline() for i in range(4)]
            rows1 = [val.strip().split(' ') for val in rows1]
            A2 = f.readline()
            A2 = int(A2.strip())        
            rows2 = [f.readline() for i in range(4)]
            rows2 = [val.strip().split(' ') for val in rows2]
        
            result = ''
            for index in xrange(len(rows1[A1 - 1])):
                val = rows1[A1 - 1][index]
                if val in rows2[A2 - 1]:
                    if not result:
                        result = val
                    else:
                        result = 'Bad magician!'
                        break
                
            if not result:
                result = 'Volunteer cheated!'
        
            resultTotal.append(result)


        for index in xrange(len(resultTotal)):
            print 'Case #{0}: {1}'.format(index + 1, resultTotal[index])

with open('a.in', 'r') as fin:
    with open('a.out', 'w') as fout:
        cases = int(fin.readline())
        for i in range(cases):
            letters = fin.readline().split()
            A = int(letters[0])
            B = int(letters[1])
            probabilities = fin.readline().split()
            probCorrectAfterPoint = []
            for j in range(len(probabilities)):
                if len(probCorrectAfterPoint)==0:
                    probCorrectAfterPoint.append(float(probabilities[j]))
                else:
                    probCorrectAfterPoint.append(probCorrectAfterPoint[(len(probCorrectAfterPoint)-1)] * float(probabilities[j]))
                    
            expectedKeepTyping = probCorrectAfterPoint[len(probCorrectAfterPoint)-1] * (B-A+1) + (1-probCorrectAfterPoint[len(probCorrectAfterPoint)-1])*(2*B-A+2)
            expectedPressEnter = B+2
                
            
            probCorrectAfterPoint.reverse()
            print probCorrectAfterPoint
            expectedBackSpace = []
            for k in range(A):
                expectedBackSpace.append( probCorrectAfterPoint[k] * (B-A+1+2*k) + (1-probCorrectAfterPoint[k])*(2*B-A+2+2*k))
            expectedBackSpace.sort()
                
            fout.write('Case #' + str(i+1) + ': ' + str("%.6f" % min(expectedBackSpace[0], expectedPressEnter, expectedKeepTyping))+ '\n');
            
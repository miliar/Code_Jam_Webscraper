'''
Google Code Jam 2010
Created by : KenKen
Created on : 2010/05/22
'''

def rotate(matrix):
    return [list(x[::-1]) for x in zip(*matrix)]

inputfile = open('A-large.in', 'r')
outputfile = open('output.txt', 'w')

inputfile.readline()   # Read the first line    
caseNo = 0
while True:
    caseNo += 1
    caseline1 = inputfile.readline().replace("\n", "")
    if not caseline1:
        break
     
    (N, K) = map(int, caseline1.split(" ")) 
    
    matrix = []
    for rows in range(N):
        matrix.append(inputfile.readline().replace("\n", ""))
    
    for (i, rows) in enumerate(matrix):
        filledLine = filter(lambda x:x != ".", rows)
        righter = '.' * rows.count(".")
        righter = list(righter)
        righter.extend(filledLine)
        matrix[i] = righter
    
    matrix = rotate(matrix)
                
    # judgement
    win = {}
    win["R"] = 0
    win["B"] = 0
    
    for i in range(N):
        if win["R"] and win["B"]:
            break
        for j in range(N):
            if matrix[i][j] == ".":
                continue
            clr = matrix[i][j]
            if win[clr]:
                continue

            #left
            (p,q) = (i,j)
            success = 1
            while success < K:
                if q - 1 < 0:
                    break
                q -= 1
                if matrix[p][q] == clr:
                    success += 1
                else:
                    break
            else:
                win[clr] = 1
                continue
            
            #right
            (p,q) = (i,j)
            success = 1
            while success < K:
                if q + 1 > len(matrix)-1:
                    break
                q += 1
                if matrix[p][q] == clr:
                    success += 1
                else:
                    break
            else:
                win[clr] = 1
                continue
            
            #up
            (p,q) = (i,j)
            success = 1
            while success < K:
                if p - 1 < 0:
                    break
                p -= 1
                if matrix[p][q] == clr:
                    success += 1
                else:
                    break
            else:
                win[clr] = 1
                continue
            
            #below
            (p,q) = (i,j)
            success = 1
            while success < K:
                if p + 1 > len(matrix)-1:
                    break
                p += 1
                if matrix[p][q] == clr:
                    success += 1
                else:
                    break
            else:
                win[clr] = 1
                continue
            
            # left-up
            (p,q) = (i,j)
            success = 1
            while success < K:
                if p - 1 < 0:
                    break
                if q - 1 < 0:
                    break
                p -= 1
                q -= 1
                if matrix[p][q] == clr:
                    success += 1
                else:
                    break
            else:
                win[clr] = 1
                continue
                        
            # right-up
            (p,q) = (i,j)
            success = 1
            while success < K:
                if p - 1 < 0:
                    break
                if q + 1 > len(matrix) - 1:
                    break
                p -= 1
                q += 1
                if matrix[p][q] == clr:
                    success += 1
                else:
                    break
            else:
                win[clr] = 1
                continue

            # left-below
            (p,q) = (i,j)
            success = 1
            while success < K:
                if p + 1 > len(matrix)-1:
                    break
                if q - 1 < 0:
                    break
                p += 1
                q -= 1
                if matrix[p][q] == clr:
                    success += 1
                else:
                    break
            else:
                win[clr] = 1
                continue
                        
            # right-below
            (p,q) = (i,j)
            success = 1
            while success < K:
                if p + 1 > len(matrix) - 1:
                    break
                if q + 1 > len(matrix) - 1:
                    break
                p += 1
                q += 1
                if matrix[p][q] == clr:
                    success += 1
                else:
                    break
            else:
                win[clr] = 1
                continue
     
    if win['B'] and win['R']:
        print >> outputfile, "Case #%d: %s" % (caseNo, "Both")
    elif win['B']:
        print >> outputfile, "Case #%d: %s" % (caseNo, "Blue")
    elif win['R']:
        print >> outputfile, "Case #%d: %s" % (caseNo, "Red")
    else:
        print >> outputfile, "Case #%d: %s" % (caseNo, "Neither")
    
inputfile.close()
outputfile.close()

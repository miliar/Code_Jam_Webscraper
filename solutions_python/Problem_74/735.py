from string import *

def solve(file):
    
    case = 0
    f = open("out_"+file,'w')
    for x in open(file):

        if case > 0:
            p = {"O":1,"B":1}
            o = 1
            moves = 0
            acc = {"O":0,"B":0}
            secuence = split(x)
            secuence.reverse()
            secuence.pop()
            
            while len(secuence) > 0:
                next = secuence.pop()
                pos = int(secuence.pop())

                if acc[next] <= abs(p[next] - pos):
                    diff = abs(p[next] - pos) + 1 - acc[next]
                    acc[next] = 0
                    if next == 'O':
                        nnext = 'B'
                    else:
                        nnext = 'O'
                    acc[nnext] += diff
                    moves += diff

                else:
                    moves += 1
                    if next == 'O':
                        nnext = 'B'
                    else:
                        nnext = 'O'
                    acc[nnext] += 1
                    acc[next] = 0

                p[next] = pos
                
            


            sol = "Case #"+str(case)+": "+str(moves)+'\n'
            f.write(sol)
        case += 1
            
            

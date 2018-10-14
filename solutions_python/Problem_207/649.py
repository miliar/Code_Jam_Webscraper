import logging
import numpy as np
import random

def horse(filename='inputA.in'):
    #reader
    rownum = 0
    numbers = list()
    j = 0
    with open('Input/' + filename, 'rb') as file:
        f = open('Output/' + filename.split('.')[0] + '.out', 'w')
        for row in file:
            # print(row)
            if rownum > 0:
                j += 1
                row = row.split()
                D = int(row[0])
                N = int(row[1])
                print('D: ' + str(D))
                print('N: ' + str(N))
                minD = 0
                for i in range(N):
                    nrow = next(file)
                    nrow = nrow.split()
                    K = int(nrow[0])
                    S = int(nrow[1])
                    loopD = (D-K)/S
                    minD = max(minD, loopD)
                f.write('Case #' + str(j) + ': ' + str(D/minD) + '\n')
                    # print('inner: ' + str(nrow))
                    
                # numbers.append(int(row.rsplit))
            rownum += 1
    # logging.debug('List of numbers: ' + str(numbers))
    
    # #writer
    # with open('Output/' + filename.split('.')[0] + '.out', 'w') as file:
    #     for i in range(len(solList)):
    #         file.write('Case #' + str(i+1) + ': ' + solList[i] + '\n')

def unicorns(filename='inputB.in'):
    #reader
    rownum = 0
    numbers = list()
    j = 0
    with open('Input/' + filename, 'rb') as file:
        f = open('Output/' + filename.split('.')[0] + '.out', 'w')
        for row in file:
            # print(row)
            if rownum > 0:
                j += 1
                row = row.split()
                N = int(row[0])
                R = int(row[1])
                O = int(row[2])
                Y = int(row[3])
                G = int(row[4])
                B = int(row[5])
                V = int(row[6])
                # print('V: ' + str(V))
                # print('Y: ' + str(Y))
                print('\n\nRound: ' + str(j))
                print('INPUT - R: ' + str(R) + '  O: ' + str(O) + '  Y: ' + str(Y) + '  G: ' + str(G) + '  B: ' + str(B) + '  V: ' + str(V))

                if (R+B < Y) or (R+Y < B) or (B+Y < R):
                    f.write('Case #' + str(j) + ': IMPOSSIBLE\n')
                    continue

                # test
                if (V+1 > Y) and (V>0):
                    if V+Y != N:
                        f.write('Case #' + str(j) + ': IMPOSSIBLE\n')
                        continue
                if V+Y == N:
                    s = ''
                    for i in range(V):
                        s += 'VY'
                    f.write('Case #' + str(j) + ': ' + s + '\n')
                    continue

                if (O+1 > B) and (O>0):
                    if O+B != N:
                        f.write('Case #' + str(j) + ': IMPOSSIBLE\n')
                        continue
                if O+B == N:
                    s = ''
                    for i in range(O):
                        s += 'OB'
                    f.write('Case #' + str(j) + ': ' + s + '\n')
                    continue

                if (G+1 > R) and (G>0):
                    if G+R != N:
                        f.write('Case #' + str(j) + ': IMPOSSIBLE\n')
                        continue
                if G+R == N:
                    s = ''
                    for i in range(G):
                        s += 'GR'
                    f.write('Case #' + str(j) + ': ' + s + '\n')
                    continue

                # algo
                print('R: ' + str(R) + '  O: ' + str(O) + '  Y: ' + str(Y) + '  G: ' + str(G) + '  B: ' + str(B) + '  V: ' + str(V))

                if (R+B < Y) or (R+Y < B) or (B+Y < R):
                    f.write('Case #' + str(j) + ': IMPOSSIBLE\n')
                    continue


                s = ''
                if O > 0:
                    s += 'B'
                    for i in range(O):
                        s += 'OB'
                    B -= (O+1)
                    O = 0

                if G > 0:
                    s += 'R'
                    for i in range(G):
                        s += 'GR'
                    R -= (G+1)
                    G = 0

                if V > 0:
                    s += 'Y'
                    for i in range(V):
                        s += 'VY'
                    Y -= (V+1)
                    V = 0

                print('s after first step: ' + str(s))
                print('R: ' + str(R) + '  O: ' + str(O) + '  Y: ' + str(Y) + '  G: ' + str(G) + '  B: ' + str(B) + '  V: ' + str(V))

                if s == '':
                    if R > B:
                        if R > Y:
                            s += 'R'
                            R -= 1
                        else:
                            s += 'Y'
                            Y -= 1
                    else:
                        if B > Y:
                            s += 'B'
                            B -= 1
                        else:
                            s += 'Y'
                            Y -= 1

                print('s if its empty: ' + str(s))
                print('R: ' + str(R) + '  O: ' + str(O) + '  Y: ' + str(Y) + '  G: ' + str(G) + '  B: ' + str(B) + '  V: ' + str(V))

                # remeber first character
                while(R + B + Y > 0):
                    # get last
                    if s[-1] == 'R':
                        if B > Y:
                            s += 'B'
                            B -= 1
                        elif Y > B:
                            s += 'Y'
                            Y -= 1
                        else:
                            if s[0] == 'B':
                                s += 'B'
                                B -= 1
                            else:
                                s += 'Y'
                                Y -= 1

                    
                    elif s[-1] == 'B':
                        if R > Y:
                            s += 'R'
                            R -= 1
                        elif Y > R:
                            s += 'Y'
                            Y -= 1
                        else:
                            if s[0] == 'R':
                                s += 'R'
                                R -= 1
                            else:
                                s += 'Y'
                                Y -= 1

                    elif s[-1] == 'Y':
                        if B > R:
                            s += 'B'
                            B -= 1
                        elif R > B:
                            s += 'R'
                            R -= 1
                        else:
                            if s[0] == 'B':
                                s += 'B'
                                B -= 1
                            else:
                                s += 'R'
                                R -= 1

                print('solution: ' + str(s))
                print('R: ' + str(R) + '  O: ' + str(O) + '  Y: ' + str(Y) + '  G: ' + str(G) + '  B: ' + str(B) + '  V: ' + str(V))

                # test start and end
                if (s[0] == s[-1]) or (R < 0) or (B < 0) or (Y < 0):
                    f.write('Case #' + str(j) + ': IMPOSSIBLE\n')
                else:
                    f.write('Case #' + str(j) + ': ' + s + '\n')

            rownum += 1




if __name__ == "__main__":

    FORMAT = '%(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    # horse('inputA.in')
    unicorns('inputB.in')













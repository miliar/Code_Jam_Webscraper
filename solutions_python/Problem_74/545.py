
if __name__ == '__main__':
    inFile = open('A-large.in', 'r')
    outFile = open('A-large.out', 'w')
    numCases = int(inFile.readline())
    print("Cases:", numCases)
    for case in range(numCases):
        outFile.write('Case #{0}: '.format(case + 1))
        data = inFile.readline().rsplit()
        data2 = []
        for i in range(int(data[0])):
            data2.append((data[i*2+1], int(data[i*2+2])))
        print(data2)

        oSteps = 0
        bSteps = 0
        oPos = 1
        bPos = 1
        total = 0
        while len(data2) > 0:
            if data2[0][0] == 'O':
                if oPos == data2[0][1]:
                    total += 1
                    bSteps += 1
                    #print('O push', data2[0][1])
                    data2.pop(0)
                    oSteps = 0
                else:
                    while oPos < data2[0][1]:
                        oPos += 1
                        if oSteps > 0:
                            oSteps -= 1
                        else:
                            #print('MOVE')
                            bSteps += 1
                            total += 1
                    while oPos > data2[0][1]:
                        oPos -= 1
                        if oSteps > 0:
                            oSteps -= 1
                        else:
                            #print('MOVE')
                            bSteps += 1
                            total += 1
            else: # 'B'
                if bPos == data2[0][1]:
                    total += 1
                    oSteps += 1
                    #print('B push', data2[0][1])
                    data2.pop(0)
                    bSteps = 0
                else:
                    while bPos < data2[0][1]:
                        bPos += 1
                        if bSteps > 0: 
                            bSteps -= 1
                        else:
                            #print('MOVE')
                            oSteps += 1
                            total += 1
                    while bPos > data2[0][1]:
                        bPos -= 1
                        if bSteps > 0:
                            bSteps -= 1
                        else:
                            #print('MOVE')
                            oSteps += 1
                            total += 1
            #print(oPos, bPos)
            #print('total:', total)
        print(total)
        outFile.write(str(total) + '\n')
    outFile.close()
    inFile.close()

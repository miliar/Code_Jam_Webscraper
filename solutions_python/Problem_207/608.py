def unicornsPlace(N, R, O, Y, G, B, V):
    #for  O G V we have only 1 posibility so
    #for O : O B O B
    #for G : G R G R
    #for V : V Y V Y
    result = ''
    if (O != 0):
        if(O > B):
            return "IMPOSSIBLE"
        else:
            for i in range(O):
                result += 'BO'
                O -= 1
                B -= 1
            if(B > 0):
                result += 'B'
            else:
                return "IMPOSSIBLE"
    if (G != 0):
        if(G > R):
            return "IMPOSSIBLE"
        else:
            for i in range(O):
                result += 'RG'
                G -= 1
                R -= 1
            if(R > 0):
                result += 'R'
            else:
                return "IMPOSSIBLE"
    if (V != 0):
        if(V > Y):
            return "IMPOSSIBLE"
        else:
            for i in range(O):
                result += 'YV'
                V -= 1
                Y -= 1
            if(Y > 0):
                result += 'Y'
            else:
                return "IMPOSSIBLE"
    letters = R + B + Y
    for i in range(letters):
        if(len(result) == 0):
            if(R > 0):
                result += "R"
                R -= 1
            elif(B > 0):
                result += "B"
                B -= 1
            elif(Y > 0):
                result += "Y"
                Y -= 1
        last = result[len(result) - 1]
        if((last == 'R') and (B != 0 or Y != 0)):
             if(B >= Y):
                 result += 'B'
                 B -= 1
                 continue
             else:
                result += 'Y'
                Y -= 1
                continue
        if(last == 'B' and (R != 0 or Y != 0)):
             if(R >= Y):
                 result += 'R'
                 R -= 1
                 continue
             else:
                 result += 'Y'
                 Y -= 1
                 continue
        if (last == 'Y' and (R != 0 or B != 0)):
            if (R >= B):
                result += 'R'
                R -= 1
                continue
            else:
                result += 'B'
                B -= 1
                continue
    if(R > 0 or Y > 0 or B > 0 ):

        return "IMPOSSIBLE"
    else:
        last = result[len(result) - 1]
        first = result[0]
        if(last == first):
            return "IMPOSSIBLE"
        else:
            return result





if(__name__ == "__main__"):
    import sys
    readFile = open(sys.argv[1])
    testCases = readFile.readline().rstrip()
    testCases = int(testCases)
    result = []
    for pos, lineNum in enumerate(range(testCases)):
        N, R, O, Y, G, B, V = readFile.readline().rstrip().split(" ")

        r = unicornsPlace(int(N), int(R), int(O), int(Y), int(G), int(B), int(V))
        result.append("Case #{}: {}\n".format(pos+1, r))
        r = ''
    readFile.close()

    writeFile = open("result.txt",'w')
    writeFile.writelines(result)
    writeFile.close()

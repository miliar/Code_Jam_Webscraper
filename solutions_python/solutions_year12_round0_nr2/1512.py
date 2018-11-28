if __name__=='__main__':
    fin = open("g:\\input.txt", 'r')
    fout = open("g:\\output", 'w')

    inpno = int(fin.readline())

    for i in range(inpno):
        inpline = fin.readline().split()
        numG = int(inpline[0])
        surpriseT = int(inpline[1])
        maxP = int(inpline[2])
        inpline = inpline[3:]

        result  = 0
        clearWin = maxP*3 - 2
        surpriseWin = clearWin -2
        for element in inpline:
            if element == '\n':
                continue
            element = int(element)
            if element >= clearWin and element >= maxP:
                result += 1
            elif element >= surpriseWin and surpriseT and element >= maxP:
                result += 1
                surpriseT -= 1

        fout.write("Case #%d: %d\n"%(i+1, result))
    fout.close()
    fin.close()

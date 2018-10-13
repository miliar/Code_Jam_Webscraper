__author__ = 'koko'


def flip(intab, start, length):
    i = start
    ilen = start+length
    nextstart = ilen
    failed = False
    while i<ilen:
        intab[i] = not intab[i]
        if not intab[i] and not failed:
            failed = True
            nextstart = i
        i+=1

    return nextstart


import fileinput




if __name__ == "__main__":
    cases = int(input())
    finput = fileinput.input()
    for t in range(1, cases + 1):
        tablen = 0
        ourtab=[]
        flipsize = 0
        result = 0

        line = finput.next()
        for char in line:
            if char == ' ':
                break

            if char == '+':
                ourtab.append(True)
            else:
                ourtab.append(False)

            tablen += 1
        # print(line)
        # print(line[tablen:len(line)-1])
        try:
            flipsize = int(line[tablen:len(line)-1])
        except:
            flipsize = int(line[tablen:len(line)])

        nextstart=0
        while nextstart < tablen and ourtab[nextstart]:
            nextstart+=1

        failed = False
        while nextstart < tablen:
            if nextstart + flipsize > tablen:
                failed = True
                break
            nextstart = flip(ourtab, nextstart, flipsize)
            result +=1
            while nextstart < tablen and ourtab[nextstart]:
                nextstart+=1
        strres = "IMPOSSIBLE" if failed else str(result)
        print("Case #"+ str(t) + ": " + strres)
        # if failed:
        #     print("Case #"+ str(t) + ": " + "IMPOSSIBLE")
        # else:
        #     print("Case #"+ str(t) + ": " + str(result))
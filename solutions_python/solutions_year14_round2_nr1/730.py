with open('A-small-attempt2.in') as file:
    cases = int(file.readline())
    output = open('output.txt','w')
    for c in range(1, cases + 1):
        words = int(file.readline())
        letterlist = []
        win = False
        n = 0
        letters = ''
        word = file.readline().rstrip('\n')
        index = []
        while(word != ''):
            l = word[0]
            j = 0
            while(word[j] == l):
                j += 1
                if j == len(word):
                    break
            index.append(j)
            word = word.lstrip(l)
            letters += l
        letterlist.append(index)
        for i in range(words-1):
            word = file.readline().rstrip('\n')
            index = []
            wordletters = ''
            while(word != ''):
                l = word[0]
                wordletters += l
                j = 0
                while(word[j] == l):
                    j += 1
                    if j == len(word):
                        break
                index.append(j)
                word = word.lstrip(l)
            letterlist.append(index)
            if wordletters != letters:
                win = True
                output.write('Case #%d: Fegla Won\n'% c)
                break
        sample = len(letterlist[0])
        tot = [0]*sample
        if not win:
            for i in letterlist:
                for j in range(sample):
                    tot[j] += i[j]
            avg = []
            for i in tot:
                avg.append(int(round(i/words,0)))
            for i in letterlist:
                for j in range(sample):
                    n += abs(i[j]-avg[j])
            output.write('Case #%d: %d\n'% (c, n))

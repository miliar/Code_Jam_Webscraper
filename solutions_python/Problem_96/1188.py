import string

fin = file('B-large.in', 'rw')
fout = file('output.txt', 'w')

numLine = 0   
for line in fin:
    if numLine == 0:
        numLine = numLine + 1
    else:
        fout.write('Case #' + str(numLine) + ': ')
        allnum = line.strip().split(' ')
        N = int(allnum[0])
        s = int(allnum[1])
        p = int(allnum[2])
        googs = 0 # number of Googlers with a score of >= p

        print( str(N) +' '+ str(s) +' ' + str(p))
#        print( range(3,N+3))

        for i in range(3, N+3):
           # print allnum[i]
            baseNum = int(allnum[i])/3
            modu = int(allnum[i])%3

            
            if int(allnum[i]) == 0 or int(allnum[i]) == 1:
                if int(allnum[i]) >= p:
                    googs += 1
                continue
    
            if int(allnum[i]) == 2:
                if 1 >= p:
                    googs += 1
                    continue
                elif s > 0:
                    if 2 >= p:
                        googs += 1
                        s -= 1
                        continue

            if baseNum >= p:
                googs += 1
            elif (modu == 1 or modu == 2) and baseNum+1 >= p:
                googs += 1
            elif modu == 0 and baseNum+1 >= p and s > 0:
                googs += 1
                s -= 1
            elif modu == 2 and baseNum+2 >= p and s > 0:
                googs += 1
                s -= 1

           # print baseNum
           # print modu

        #sentenceList = []
        #for letter in line:
        #    if letter == '\n':
        #        continue
        #    translatedLetter = codeToEng[letter]
        #    # print translatedLetter + '\n'
        #    sentenceList.append(translatedLetter)

        numLine = numLine + 1
        fout.write(str(googs))
        fout.write('\n')

fin.close()
fout.close()

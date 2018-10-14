fin = open('D-large.in.txt','r')

fout = open('output.txt', 'w')

numCases = int(fin.readline())

for cases in range(numCases):
    sizeLst = [int(x) for x in fin.readline().split()]
    size = sizeLst[0]
    Naomi = [float(x) for x in fin.readline().split()]
    Ken = [float(x) for x in fin.readline().split()]

    Naomi.sort()
    Ken.sort()

    j = 0
    jj = size
    for i in range(size):
        if Naomi[i] > Ken[j]:
            j = j + 1
        else:
            jj = jj - 1

    fout.write("Case #" + str(cases+1) + ": "+str(jj)+" ")

    j = 0
    NaomiWinWar = 0
    for i in range(size):
        while j < size and Naomi[i]>Ken[j]:
            j = j+1
        if j>=size:
            NaomiWinWar = size-i
            break
        else:
            j = j+1
    fout.write(str(NaomiWinWar)+'\n')


fin.close()
fout.close()
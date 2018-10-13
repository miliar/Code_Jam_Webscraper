
def flip(panc, pos, k):
    for i in range(pos,pos+k):
        if panc[i] == '+':
            panc[i] = '-'
        else:
            panc[i] = '+'
    
            
fin = open("input.txt", "r")
fout = open("output.txt","w")
tFile = fin.readlines()
t = int(tFile.pop(0).strip('\n'))


for numLine in range(0,t):
    line = tFile.pop(0).strip('\n').split(' ')

    k = int(line[1])
    panc = list(line[0])

    flippable = True
    numFlips = 0
    for i in range(0, len(panc)):
        if i + k > len(panc):
            for j in range(i,len(panc)):
                if panc[j] == '-':
                    flippable = False
            break
        if panc[i] == '-':
            flip(panc,i,k)
            numFlips+=1
        

    print("Case #" + str(numLine+1) + ': ', end='')
    print("Case #" + str(numLine+1) + ': ', end='', file=fout)
    if flippable == True:
        print(numFlips)
        print(numFlips, file=fout)
    else:
        print("IMPOSSIBLE")
        print("IMPOSSIBLE", file=fout)

fout.close()
fin.close()

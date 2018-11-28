

fin = open('B-large.in')
T = int(fin.readline().split()[0])
print(T)

sNumsIn = []
for i in range(T):
    sNumsIn.append(fin.readline().split()[0])
    
numsOut = []
for sIn in sNumsIn:
    lOut = ['0'] + list(sIn)
    for j in range(len(lOut) - 1, 0, -1):
        if lOut[j] >= lOut[j - 1]:
            continue
        k = j;
        while k < len(lOut) and lOut[k] != '9':
            lOut[k] = '9';
            k += 1
        lOut[j - 1] = str(int(lOut[j - 1]) - 1)
    sOut = ''.join(lOut[1::])
    numsOut.append(int(sOut))

with open('tidy_out.txt', 'w') as fout:
    for i in range(len(numsOut)):
        fout.write('Case #' + str(i + 1) + ': ' +
                   str(numsOut[i]) + '\n')


        

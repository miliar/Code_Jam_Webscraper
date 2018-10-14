file = open('C:/Users/ja13/Desktop/cj2015Files/A-large.in','r')
filew = open('C:/Users/ja13/Desktop/cj2015Files/A-large-0-out.txt','w+')

numCases = int(file.readline())

for casenum in range(1,numCases+1):
    line = file.readline()
    Smax = int(line.split()[0])
    vals = line.split()[1]
    Sattained = 0
    Srequired = 0
    answer = 0
    for c in vals:        
        if Srequired == 0 and int(c) == 0:
            answer = answer + 1
            Sattained = Sattained + 1
        else:
            if int(c) !=0 :
                while Srequired > Sattained:
                    Sattained = Sattained + 1
                    answer = answer + 1
        Srequired = Srequired + 1
        Sattained = Sattained + int(c)
    filew.writelines('Case #'+str(casenum)+': '+ str(answer)+'\n')
    print('Case #'+str(casenum)+': '+ str(answer)+'\n')

file.close()
filew.flush()
filew.close()
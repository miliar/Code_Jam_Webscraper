fin = open(input('input file: '))
fout = open(input('output file: '),'w')
T = int(fin.readline())
frase = 'welcome to code jam'
for testnum in range(1,T+1):
    s = fin.readline()
    u = [0]*(len(frase))+[1]
    for c in range(len(s)):
        for fc in range(len(frase)-1,-1,-1):
            if s[c]==frase[fc]:
                u[fc]+=u[fc-1]
                u[fc]%=10000
    fout.write('Case #'+ str(testnum)+': '+str(10000+u[len(frase)-1])[1:]+'\n')
fin.close()
fout.close()
    

from decimal import *
fInput = open('test.in','r')
fOutput = open('output.txt','w')
t = int(fInput.readline())
getcontext().prec = 7
for i in range(1,t+1):
    data = map(float,fInput.readline().split())
    dT = data[2]/2
    pT = dT + 1
    up = 1
    upT = [data[0]/2]
    while True :
        cookie = ((data[1]*up)+2)
        pT = upT[-1]+(data[2]/cookie)
        if pT > dT:
            break
        dT = pT
        up += 1
        upT.append(data[0]/cookie+upT[-1])
    fOutput.write("Case #"+str(i)+": "+str(dT)+'\n')
fOutput.close()
        

file=open('testin3.txt')
out=open('output.txt','w')
T = int(file.readline())
for i in range(0,T):
    line = file.readline()
    obut = []
    bbut = []
    buts = []
    info = line.split(" ")
    numbut = int(info[0])
    for j in range(1,numbut+1):
        ty = info[2*j-1]
        num = info[2*j]
        if ty=='O':
            obut.append(int(num))
            buts.append((1,int(num)))
            #1=orange, 2=blue
        else:
            bbut.append(int(num))
            buts.append((2,int(num)))
    opos = 1
    bpos = 1
    count = 0
    oindex = 0
    bindex = 0
    butpres = 0
    while butpres < numbut:
        nextty = buts[butpres][0]
        if oindex < len(obut):
            nexto = obut[oindex]
            diffo = nexto-opos
            if diffo > 0:
                opos=opos+1
            elif diffo < 0:
                opos=opos-1
            else:
                if nextty==1:
                    butpres=butpres+1
                    oindex=oindex+1
                    
        if bindex < len(bbut):
            nextb = bbut[bindex]
            diffb = nextb-bpos
            if diffb > 0:
                bpos=bpos+1
            elif diffb < 0:
                bpos=bpos-1
            else:
                if nextty==2:
                    butpres=butpres+1
                    bindex=bindex+1
        count = count+1
##        print(bpos)
##        print(opos)
##        print(count)
    out.write('Case #')
    out.write(str(i+1))
    out.write(': ')
    out.write(str(count))
    out.write('\n')
out.close()
file.close()

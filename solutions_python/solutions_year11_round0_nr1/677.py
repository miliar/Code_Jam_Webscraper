import csv
import collections

def botTrust(fname):

    infile=open(fname,'rb')
    reader=csv.reader(infile, delimiter=' ')

    outfile=open('bottrust.dat','wb') 
    writer=csv.writer(outfile,delimiter=' ')

    buttonlist=collections.defaultdict(lambda:[])

    for row in reader:
        numcases=int(row[0])
        break
    case=1
    for row in reader:
        buttons=int(row[0])
        #print(buttons)
        lenrow=1+2*buttons
        robots=[]
        btarget=0
        otarget=0
        bButtons=[]
        oButtons=[]
        bwork=False
        owork=False
        pushed=0
        for i in xrange(1,lenrow,2):
            robots.append(row[i])
            if row[i]=='B':
                bButtons.append(int(row[i+1]))
                btarget+=1
            else:
                oButtons.append(int(row[i+1]))
                otarget+=1

        bpos=1
        opos=1
        if btarget>0:
            bwork=True
        if otarget>0:
            owork=True
        pushed=0
        opushed=0
        bpushed=0
        timer=1

        #print(robots)
        #print(bButtons)
        #print(oButtons)
        while True:
            move=False
            if owork==True:
                if robots[pushed]=='O' and oButtons[opushed]==opos:
                    opushed+=1
                    move=True
                    #print('o push')
                    if opushed==otarget:
                        owork=False
                elif oButtons[opushed]<opos:
                    opos-=1
                elif oButtons[opushed]>opos:
                    opos+=1
                    
            if bwork==True:
                if robots[pushed]=='B' and bButtons[bpushed]==bpos:
                    bpushed+=1
                    move=True
                    #print('b push')
                    if bpushed==btarget:
                        bwork=False
                elif bButtons[bpushed]<bpos:
                    bpos-=1
                elif bButtons[bpushed]>bpos:
                    bpos+=1

            if move==True:
                pushed+=1
                #print(pushed)
                #print(timer)
            if pushed==buttons:
                break
            timer+=1
        mystring='Case #'+str(case)+': '+str(timer)+'\n'
        #print(mystring)
        outfile.write(mystring)
        case+=1

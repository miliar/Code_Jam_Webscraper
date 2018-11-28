f=file('A-large.in','r')
inp=[]
for line in f:
    if '\n' in line:
        line=line[:-1]
    inp.append(line)
f.close()

f=file('something.out','w')

def checkBDes(n):
    if bot['B']!=BDes:
        if BDes>bot['B']:
            bot['B']+=1
        else:
            bot['B']-=1

def checkODes(n):
    if bot['O']!=ODes:
        if ODes>bot['O']:
            bot['O']+=1
        else:
            bot['O']-=1

N=inp[0]
inp.remove(N)
casenum=1

for case in inp:
    sec=0
    bot={'O':1,'B':1}
    ODes=1
    BDes=1
    case=case.split(' ')
    M=case[0]
    case=case[1:]
    index=0
    for n,i in enumerate(case):
        if i=='O':
            ODes=int(case[n+1])
            break
    for n,i in enumerate(case):
        if i=='B':
            print case
            BDes=int(case[n+1])
            break

    
    while True:
        if case[index]=='O':
            if int(case[index+1])==bot['O']:
                sec+=1
                checkBDes(0)
                case[index]=None
                for n,i in enumerate(case):
                    if i=='O':
                        ODes=int(case[n+1])
                        break
                print ODes
            else:
                if int(case[index+1])>bot['O']:
                    while int(case[index+1])>bot['O']:
                        bot['O']+=1
                        sec+=1
                        checkBDes(1)
                    sec+=1
                    case[index]=None
                    for n,i in enumerate(case):
                        if i=='O':
                            ODes=int(case[n+1])
                            break
                    print ODes
                    checkBDes(1)
                else:
                    while int(case[index+1])<bot['O']:
                        bot['O']-=1
                        sec+=1
                        checkBDes(1)
                    sec+=1
                    case[index]=None
                    for n,i in enumerate(case):
                        if i=='O':
                            ODes=int(case[n+1])
                            break
                    checkBDes(1)
                    print ODes
        else:
            if int(case[index+1])==bot['B']:
                sec+=1
                checkODes(0)
                case[index]=None
                for n,i in enumerate(case):
                    if i=='B':
                        BDes=int(case[n+1])
                        break
                print BDes
            else:
                if int(case[index+1])>bot['B']:
                    while int(case[index+1])>bot['B']:
                        bot['B']+=1
                        sec+=1
                        checkODes(1)
                    case[index]=None
                    for n,i in enumerate(case):
                        if i=='B':
                            BDes=int(case[n+1])
                            break
                    sec+=1
                    checkODes(1)
                else:
                    while int(case[index+1])<bot['B']:
                        bot['B']-=1
                        sec+=1
                        checkODes(1)
                    case[index]=None
                    for n,i in enumerate(case):
                        if i=='B':
                            BDes=int(case[n+1])
                            break
                    sec+=1
                    checkODes(1)
        index+=2
        if index>len(case)-2:
            f.write('Case #%i: %i\n'%(casenum,sec))
            casenum+=1
            break
f.close()

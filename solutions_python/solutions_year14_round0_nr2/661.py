#f = open('B-small-attempt0.in', 'r')
f = open('B-large.in', 'r')
outpu=open('output.txt','w')
cases = int(f.readline())
for case in range(cases):
    [C,F,X] = [float(x) for x in f.readline().split(" ")]
    old = X/2
    passed  = 0
    inc =2
    goOn = True
    while(goOn):
        passed =  passed + C/inc
        inc =inc+F
        time = passed + X/inc
        goOn = time <old
        if goOn:
            old=time
    outpu.write('Case #'+str(case+1)+": "+str(old)+'\n')
f.close()
outpu.close()

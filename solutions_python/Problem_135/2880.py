import fileinput

leggi=fileinput.input()
numCases=(int)(leggi.readline())
for i in range(numCases):
    val=[]
    lprima=[]
    lseconda=[]
    compare={}
    prima=(int)(leggi.readline())
    for pi in range(4):
        val=leggi.readline().split(' ')
        val[-1]=val[-1].strip()
        if pi==(prima-1):
            lprima=val
    seconda=(int)(leggi.readline())
    for si in range(4):
        val=leggi.readline().split()
        val[-1]=val[-1].strip()
        if si==(seconda-1):
            lseconda=val
    compare=set(lprima).intersection(set(lseconda))
    print('Case #'+str(i+1)+": ",end='')
    if (len(compare) == 1) :
        print(list(compare)[0])
    if (len(compare) > 1) :
        print('Bad magician!')
    if (len(compare) == 0):
        print('Volunteer cheated!')


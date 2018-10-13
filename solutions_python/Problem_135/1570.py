f = open("A-small-attempt0.in",'r')

output = open('aoutput.txt','w')

ncases = int(f.readline())



for T in range(0,ncases):
    firstanswer = int(f.readline())
    firstline = []
    for i in range(0,4):
        if (i + 1) == firstanswer:
            firstline = map(int, f.readline().split())
        else:
            f.readline()
    secondanswer = int(f.readline())
    secondline = []
    for i in range(0,4):
        if (i + 1) == secondanswer:
            secondline = map(int, f.readline().split())
        else:
            f.readline()
    print firstline, secondline

    intersection = []
    for i in firstline:
        if i in secondline:
            intersection.append(i)

    print intersection

    if len(intersection) == 0:
        output.write('Case #'+str(T+1)+': Volunteer cheated!\n')
    elif len(intersection) == 1:
        output.write('Case #'+str(T+1)+': '+str(intersection[0])+'\n')
    else:
        output.write('Case #'+str(T+1)+': Bad magician!\n')

output.close()

f = open('C:/Users/rajiv/Desktop/code jam 15/A-large.out', 'w')
lines = [line.strip() for line in open('C:/Users/rajiv/Desktop/code jam 15/A-large.in')]
result=0

for i in range(1, int(lines[0]) + 1):
    j = lines[i].split()
    j=map(int,j)
    j[1:3] = sorted(j[1:3],reverse=True)
    print j
    if j[0]==1 :
        winner='GABRIEL'

    elif j[0]==2:
        if (j[1]*j[2])%2==0:
            winner='GABRIEL'

        else :
            winner='RICHARD'

    elif j[0]==3 :
        if j[1:3] in ([3,2],[3,3],[4,3]) :
            winner='GABRIEL'

        else :
            winner='RICHARD'

    elif j[0]==4 :
        if j[1:3] in [4,4] :
            winner='GABRIEL'

        else :
            winner='RICHARD'

    print 'Case #'+i.__str__()+': '+winner
    f.write('Case #'+i.__str__()+': '+winner+'\n')


f.close()


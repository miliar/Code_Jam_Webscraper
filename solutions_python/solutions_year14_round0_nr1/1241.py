fin = open ('A-small-attempt0.in','r')
fout = open('CJAM1OUT.txt','w')
T = int(fin.readline().strip())

for j in range(T):
    fq = int(fin.readline().strip())-1
    grid1 = []
    grid2 = []
    solns = []

    for i in range(4):
        grid1.append(fin.readline().strip().split())
        
    sq = int(fin.readline().strip())-1
    for i in range(4):
        grid2.append(fin.readline().strip().split())

    solns = (set(grid1[fq]).intersection(grid2[sq]))

    #print (len(solns))

    if len(solns) == 1:
        print ('Case #', end = '', file = fout)
        print (j+1, end = '',file = fout)
        print (':',list(solns)[0],file = fout)
    elif len(solns) > 1:
        print ('Case #', end = '',file = fout)
        print (j+1, end = '',file = fout)
        print (': Bad magician!',file = fout)
    elif len(solns) == 0:
        print ('Case #', end = '',file = fout)
        print (j+1, end = '',file = fout)
        print (': Volunteer cheated!',file = fout)

    #print (grid1[fq], grid2[sq])
fout.close()

fin = open('A-small-attempt0.in','r')
fout = open('magic.out','w')

cases = int(fin.readline().strip())
a = 0

while a < cases:

    firstRow = int(fin.readline().strip())

    FCardsOne = fin.readline().split()
    FCardsTwo = fin.readline().split()
    FCardsThree = fin.readline().split()
    FCardsFour = fin.readline().split()

    InitialCards = FCardsOne+FCardsTwo+FCardsThree+FCardsFour

    secondRow = int(fin.readline().strip())

    LCardsOne = fin.readline().split()
    LCardsTwo = fin.readline().split()
    LCardsThree = fin.readline().split()
    LCardsFour = fin.readline().split()

    LastCards = LCardsOne+LCardsTwo+LCardsThree+LCardsFour

    count = 0
    match = []
    #print(firstRow,secondRow)
    #print(InitialCards[(firstRow-1)*4:((firstRow-1)*4)+4])
    #print(LastCards[(secondRow-1)*4:((secondRow-1)*4)+4])

    for b in InitialCards[(firstRow-1)*4:((firstRow-1)*4)+4]:
        if b in LastCards[(secondRow-1)*4:((secondRow-1)*4)+4]:
            count+=1
            match.append(b)
    if count==0:
        print('Case #'+(str(a+1))+': Volunteer cheated!')
    elif count == 1:
        print('Case #'+(str(a+1))+ ': ' + match[0])
    else:
        print('Case #'+(str(a+1))+': Bad magician!')

    a+=1
        

    

    

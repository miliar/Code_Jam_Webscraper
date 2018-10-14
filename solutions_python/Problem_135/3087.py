file=open('c:/Users/pihulic/Desktop/CODEJAM/A-small-attempt3.in')

T=int(file.next().rstrip('\n'))

for x in range(T):
    CARDS1=[]    
    CARDS2=[]
    MATCHES=0

    R1=int(file.next().rstrip('\n'))

    CARDS1.append(file.next().rstrip('\n').split())
    CARDS1.append(file.next().rstrip('\n').split())
    CARDS1.append(file.next().rstrip('\n').split())
    CARDS1.append(file.next().rstrip('\n').split())

    R2=int(file.next().rstrip('\n'))

    CARDS2.append(file.next().rstrip('\n').split())
    CARDS2.append(file.next().rstrip('\n').split())
    CARDS2.append(file.next().rstrip('\n').split())
    CARDS2.append(file.next().rstrip('\n').split())

    for card1 in CARDS1[R1-1]:
        for card2 in CARDS2[R2-1]:
            if card1==card2:
                MATCHES+=1
                match=card1

    if MATCHES==1:
        print('Case #'+str(x+1)+': ' + match)

    elif MATCHES>1:
        print('Case #'+str(x+1)+': Bad magician!')

    elif MATCHES==0:
        print('Case #'+str(x+1)+': Volunteer cheated!')


        

    
    
    
    


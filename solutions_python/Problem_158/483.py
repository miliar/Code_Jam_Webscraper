def read_words(afile):
    words = []
    for line in afile:
            words.append(line.strip())
    return words


filename = open('poop.txt' , 'r')
T = filename.readline() #num test cases
aList = read_words(filename) # array where each element is a line of text

for i in range(int(T)):
    line = aList[i].split()
    X = int(line[0])
    R = int(line[1])
    C = int(line[2])
    if(X > 6):
        print("Case #"+str(i+1)+": RICHARD")
    else:
        if ((R*C)%X != 0):
            print("Case #"+str(i+1)+": RICHARD")
        elif (X==1):
            print("Case #"+str(i+1)+": GABRIEL")
        elif (X==2):
            if (((R%2)==1) and ((C%2)==1)):
                print("Case #"+str(i+1)+": RICHARD")
            else:
                print("Case #"+str(i+1)+": GABRIEL")
        elif (X==3):
            if ( ((R>=3) and (C>=3)) or ((R==2) and (C==3)) or ((R==3) and (C==2)) ):
                print("Case #"+str(i+1)+": GABRIEL")
            else:
                print("Case #"+str(i+1)+": RICHARD")
        elif (X==4):
            if ( ((R>=4) and (C>=4)) or ((R==4) and (C==3)) or ((R==3) and (C==4)) ):
                print("Case #"+str(i+1)+": GABRIEL")
            else:
                print("Case #"+str(i+1)+": RICHARD")
        elif (X==5):
            if ( ((R<4)and(C<5)) or ((R<5)and(C<4)) ):
                print("Case #"+str(i+1)+": RICHARD")
            else:
                print("Case #"+str(i+1)+": GABRIEL")
        elif (X==6):
            if ( (R<6)and(C<6) ):
                print("Case #"+str(i+1)+": RICHARD")
            else:
                print("Case #"+str(i+1)+": GABRIEL")


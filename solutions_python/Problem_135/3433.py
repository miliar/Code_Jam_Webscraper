f = open('A-small-attempt2.in', 'r')

T = f.readline()
y = 1

iterator = 0

for x in xrange(0,int(T)):
    firstRow,secondRow = -6,-6
    for i in xrange(0,10):
        if (i == 0):
            firstRow = int(f.readline())
            
        elif (i == firstRow):
            a = f.readline().split(' ')
            
        elif (i == 5):
            secondRow = int(f.readline())
            
        elif (i == 5+secondRow):
            b = f.readline().split(' ')
            
        else:
            f.readline()
    for num in a:
        num = int(num)
        for num2 in b:
            num2 = int(num2)
            if (num == num2):
                y = num
                iterator = iterator+1

    if (iterator == 0):
        print("Case #" + str(x+1) + ": Volunteer cheated!")
    elif (iterator == 1):
        print("Case #" + str(x+1) + ": " + str(int(y)))
    elif (iterator > 1):
        print("Case #" + str(x+1) + ": Bad magician!")
    iterator = 0
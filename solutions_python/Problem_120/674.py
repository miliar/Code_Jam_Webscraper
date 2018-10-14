


def calculateArea(radius, mili):
    actualMili = 0
    actualRadius = radius
    stripes = 0
    while (actualMili < mili):
        used = (2*actualRadius+1)
        actualMili = actualMili + used
        actualRadius = actualRadius + 2
        if actualMili > mili:
            break
        else:
            stripes = stripes + 1
    if stripes > 0:
        return stripes
    else:
        return 1
    
    

if __name__ == "__main__":

    numberOfTests = (int)(input())
    
    info = []    
    
    for a in range(numberOfTests):
            info = (input().split(' '))
            print('Case #'+str(int(a)+1)+': '+str(calculateArea(int(info[0]),int(info[1]))))
        
    
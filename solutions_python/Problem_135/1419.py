'''
Created on 12/04/2014

'''


NROWS = 4


def processCase(row1, row2):
    intersection = row1.intersection(row2)
    l = len(row1.intersection(row2))
    
    if l == 1:
        return str(intersection.pop())
    elif l == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'
    
    return str(row1.intersection(row2))
    

if __name__ == '__main__':
    myinput = open('A-small-attempt0.in', 'r')
    myoutput = open('A-small-attempt0.out', 'w')
    
    T = int(myinput.readline())
    
    for t in range(T):
        chosenRow1 = int(myinput.readline()) - 1
        for i in range(NROWS):
            row = set(map(int, myinput.readline().split()))
            if i == chosenRow1:
                row1 = row
        
        chosenRow2 = int(myinput.readline()) - 1
        for i in range(NROWS):
            row = set(map(int, myinput.readline().split()))
            if i == chosenRow2:
                row2 = row  
        
        myoutput.write('Case #' + str(t+1) + ": " + processCase(row1, row2) + '\n')
    
    myoutput.close()
    myinput.close()
    pass
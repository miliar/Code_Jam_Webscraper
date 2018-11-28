# 2013Q A

from copy import deepcopy

# Obtain T
T = int(input())

def check_notcompleted(row):
    for i in range(4):
        if '.' in row[i]:
            return True 
    return False

def won(A,row):
    # check horizontal wins
    for i in range(4):
        if row[i]==A+A+A+A:
            return True
        elif row[0][i]+row[1][i]+row[2][i]+row[3][i]==A+A+A+A:
            return True
        elif row[0][0]+row[1][1]+row[2][2]+row[3][3]==A+A+A+A:
            return True
        elif row[3][0]+row[2][1]+row[1][2]+row[0][3]==A+A+A+A:
            return True
    return False


for a in range(T):
    Done = False

    row=['','','','']
    temprow=['','','','']

    # Store the board
    for i in range(4):
        row[i]=input()
    
    # Check if O won
    for i in range(4):
        temprow[i]=row[i].replace('T','O')
    if won('O',temprow):
        print('Case #'+str(a+1)+': O won')
        k=input()
        continue

    # Check if X won
    for i in range(4):
        temprow[i]=row[i].replace('T','X')
    if won('X',temprow):
        print('Case #'+str(a+1)+': X won')
        k=input()
        continue

    if check_notcompleted(row):
        print('Case #'+str(a+1)+': Game has not completed')
        k=input()
        continue

    print('Case #'+str(a+1)+': Draw')
    k=input()

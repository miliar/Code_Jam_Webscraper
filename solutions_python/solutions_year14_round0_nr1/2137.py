#__author__ = 'afonso-ferreira'
import sys

file = open('magic.txt', 'r')
matrix=file.read().split('\n')
#print(matrix)

for aux in range(0,int(matrix[0])):
    stack=matrix[aux*10+int(matrix[aux*10+1])+1]
    stack=stack.split(' ')
    #print(set(stack))
    #print(set(matrix[aux*10+int(matrix[aux*10+6])+6].split(' ')))
    stack=list(set(stack)& set(matrix[aux*10+int(matrix[aux*10+6])+6].split(' ')))
    #print(stack)
    if(stack==[]):
        print('Case #',end="")
        print(aux+1,end="")
        print(": Volunteer cheated!")
    elif(len(stack)>1):
        print('Case #',end="")
        print(aux+1,end="")
        print(": Bad magician!")
    else:
        print('Case #',end="")
        print(aux+1,end="")
        print(":",stack[0])
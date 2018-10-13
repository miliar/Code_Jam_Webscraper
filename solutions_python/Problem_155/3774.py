import os

file = open('test1.txt')
line = file.readlines()

def solveCase():
    answer = 0
    for x in range(1, int(line[0])+1):
        guests = 0
        people_clapping = 0
        value = int(line[x][0])
        for y in range(2, value + 2):
            ahead = y - 1
            people = int(line[x][y])
            people_clapping = people_clapping + people
            while people_clapping + guests < ahead:
                guests = guests + 1     
        printCase(x, guests)

def printCase(case, answer):
    print "Case #"+str(case)+": "+str(answer)

if __name__ == "__main__":
    solveCase()

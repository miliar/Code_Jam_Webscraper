import sys
import math
import string

def ReadFile(filename):
    file = open(filename)
    n = int(file.readline())
    for case in range(1,n+1):
        line = file.readline()
        line_lst = str.split(line)
        print("Case #" + str(case) + ": " + CountFairAndSquares(line_lst[0], line_lst[1]))



def CountFairAndSquares(start, end):
    count = 0
    for i in range(math.ceil(math.sqrt(int(start))), math.floor(math.sqrt(int(end))+1)):
        if IsFair(i) and IsSquare(i):
            count += 1
    return str(count)

def IsFair(num):
    num = str(num)
    for i in range(len(num)//2):
        if num[i]!=num[-(i+1)]:
            return False
    return True


def IsSquare(num):
    num = str(int(num)**2)
    for i in range(len(num)//2):
        if num[i]!=num[-(i+1)]:
            return False
    return True    









if __name__ == '__main__':
    ReadFile(sys.argv[1])
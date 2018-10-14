import math

def numbersInLine(num,line):
    n0 = int(math.log(num,2))
    numofNum = 2**(line-1)
    rem = num - 2**n0
    div = rem//numofNum
    mod = rem%numofNum
    baseNumber = 2**(n0-line+1) + div
    numberOfLargerNum = mod
    numberOfBaseNum = numofNum - numberOfLargerNum

    return (baseNumber,numberOfBaseNum,numberOfLargerNum)


def numCoord(m):
    m0 = int(math.log(m+1,2))
    mod = m - 2**m0 + 1
    if mod !=0:
        m0 = m0+1
    else:
        mod = 2**(m0-1)
    return (m0,mod)



def answer(num,p):

    (line,col) = numCoord(p)
    (baseNumber, numberOfBaseNum, numberOfLargerNum) = numbersInLine(num + 1, line)
    if col <= numberOfLargerNum:
        res = baseNumber + 1
    else:
        res = baseNumber
    if res%2 == 1:
        return ( res//2,res//2 -1)
    else:
        return ( res//2 -1 , res//2 -1 )



import sys

def main():

    with open(sys.argv[1]) as f:
        nums = int(f.readline())

        for x in range(nums):
            N,K = f.readline().strip().split()
            N,K = int(N),int(K)

            y,z = answer(N,K)
            print("Case #{:d}: ".format(x+1)+str(y) +' '+str(z))

main()

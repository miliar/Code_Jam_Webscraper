from sys import stdin
import math

N = int(input())

def isPalindrome(j):
    number = str(j)
    lenNumber = len(number)
    good = True
    for i in range(lenNumber//2):
        if number[i] != number[lenNumber - i - 1]:
            good = False
    return good

for i in range(N):
    A,B = map(int, input().split())
    sA = math.floor(math.sqrt(A))
    sB = math.ceil(math.sqrt(B))+1

    nbFairAndSquare = 0
    for j in range(sA, sB):
        if isPalindrome(j) and isPalindrome(j*j) and j*j >= A and j*j <= B:
            # print(j, j*j)
            nbFairAndSquare += 1

    print('Case #{}: {}'.format(i+1, nbFairAndSquare))

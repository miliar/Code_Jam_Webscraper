import os
import math
from math import sqrt

index=open("input.txt","r")
r=index.readline()
nb_case = int(r)
r=index.readline()


R=open("resultat.txt","w")
R.close()



def test_palindrome(S):
    S = str(S)
    for i in range(int(len(S)/2)+1):
        if S[i]!= S[len(S)-1-i]:
            # print False
            return False
            break
    # print True
    return True


def test_square_palindrome(S):
    #int square
    sqrt_int = int(math.sqrt(int(S)))
    if sqrt_int ** 2 ==S:
        if test_palindrome(sqrt_int):
            return True
        else:
            return False
    else:
        # print False
        return False

def test_fair_and_square(S):
    if test_square_palindrome(S):
        if test_palindrome(S):
            return str(S)

line=1
while r!="":
    
    n=0
    a,b = r.rstrip('\n\r').split(" ")
    a,b=int(a),int(b)
    for i in range(a,b+1):
        if test_fair_and_square(i):
            n+=1
    R=open("resultat.txt","a")
    R.write("Case #" + str(line) + ": " + str(n) + "\n")
    r=index.readline()
    line+=1


# print test_square_palindrome(1)
# print test_palindrome(1)
# print test_fair_and_square(1)

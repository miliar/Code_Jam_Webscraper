import math
f = open("gjc33in.txt","r")

T = int(f.readline().strip())

def isPalindrome(s):
    for i in range(len(s)/2):
        if s[i]!=s[-(i+1)]:
            return False
    return True
for case in range(1,T+1):
    print "Case #" + str(case)+":",
    A,B=map(int,f.readline().strip().split(" "))
    count=0
    i=int(math.sqrt(A))
    if i**2<A:
        i+=1
    while (i**2<=B):
        if isPalindrome(str(i)) and isPalindrome(str(i**2)):
            count+=1
        i+=1
    print count

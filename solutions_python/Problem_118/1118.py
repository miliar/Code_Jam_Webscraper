from math import sqrt

testcases = int(input())
count = 1

def is_palindrome(word):
   for i in range(len(word)//2):
         if word[i] != word[-1-i]:
                 return False
   return True
  
while(testcases) :
    A, B = input().split()
    sol = 0
    A = int(A)
    B = int(B)
    lower = int(sqrt(A))
    if(lower*lower < A):
        lower = lower+1
    for root in range(lower, int(sqrt(B))+1 ):
        number = root*root
        numString = str(number)
        if(numString[-1] in '02378' or len(numString)%2 is 0):continue
        if(is_palindrome(numString)):
            if(is_palindrome(str(root))):
                sol = sol + 1
    print("Case #"+str(count)+": "+str(sol))
    count = count+1
    # print(sol)
    testcases = testcases -1
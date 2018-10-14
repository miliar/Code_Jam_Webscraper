def IsPalindrome(inpstr):
    #inpstr = str(inpstr)
    lt = len(inpstr)
    palindrome = True
    i = 0
    for i in range(lt):
        #        print(inpstr[i], inpstr[-i-1], i)
        if inpstr[i] != inpstr[-i - 1]:
           palindrome = False
           break
    return palindrome

for i in range (10**50):
    if IsPalindrome(str(i)) and IsPalindrome(str(i*i)):
        print (i*i)
# precalculates numbers up to large output 1

def isPalindrome(x):
    strX = str(x)
    for i in range((len(strX) // 2) + 1):
        if strX[i] != strX[-i-1]:
            return False
    return True

numbers = []
for i in range(10000001):
#for i in range(1001):
    if isPalindrome(i) and isPalindrome(i * i):
        numbers.append(i * i)

print(numbers)
        
    
def isPalindrome(num):
    rev = str(num)[::-1]
    if(str(num)==rev):
        return True
    return False
def isSquareRootPalindrome(num):
    sqrt = num ** 0.5
    if(int(sqrt) == sqrt):
        return isPalindrome(int(sqrt))
    return False
    
f = open('3i.in','r')
f2 = open('3o.txt','w')
n = f.readline()
for i in range(1, int(n)+1):
    txt = f.readline()
    numbers = txt.split(' ')
    count = 0
    for num in range(int(numbers[0]),int(numbers[1])+1):
        if(isPalindrome(num) and isSquareRootPalindrome(num)):
            ##print num
            count = count + 1
    result = 'Case #'+str(i)+': '+ str(count)
    print result
    f2.write(result+'\n')
f.close()
f2.close()



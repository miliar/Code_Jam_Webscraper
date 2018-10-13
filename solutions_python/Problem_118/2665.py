def isPalindrome(num):
    rev = str(num)[::-1]
    if(str(num)==rev):
        return True
    return False

def isSquareRootPalindrome(num):
    sqrt = num ** 0.5
    if(long(sqrt) == sqrt):
        return isPalindrome(long(sqrt))
    return False

def myxrange(a1, a2=None, step=1):
    if a2 is None:
        start, last = 0, a1
    else:
        start, last = a1, a2
    while cmp(start, last) == cmp(0, step):
        yield start
        start += step

f = open('3i.in','r')
f2 = open('3o.txt','w')
n = f.readline()
##print n
for i in range(1, int(n)+1):
    txt = f.readline().strip()
    numbers = txt.split(' ')
    count = 0
    ##print numbers
    for num in xrange(long(numbers[0]),long(numbers[1])+1):
        if(isPalindrome(num) and isSquareRootPalindrome(num)):
            print num
            count = count + 1
    result = 'Case #'+str(i)+': '+ str(count)
    print result
    f2.write(result+'\n')
f.close()
f2.close()



import math

def isPalindrome(n):
    string = str(n)
    if (string == string[::-1]):
        return True
    else:
        return False

t = int(raw_input())
for i in range(1, t + 1):
    data = raw_input()
    data = data.split()
    a = int(data[0])
    b = int(data[1])
    start = int(math.ceil(math.sqrt(a)))
    end = int(math.floor(math.sqrt(b)))
    total = 0
    for num in range(start, end + 1):
        if isPalindrome(num):
            sqr = num**2
            if isPalindrome(sqr):
                total += 1
    print "Case #" + str(i) + ": " + str(total)
 

import math

def isPalindrome(num):
    if not float(num).is_integer():
        return False
    
    initialStr = str(int(num))
    reverseStr = initialStr[::-1]

    if initialStr == reverseStr:
        return True

    return False
    

i = open('C-small-attempt0.in', 'r+')
o = open('output.txt', 'w+')

text = i.readlines()
num = int(text[0])
del[text[0]]

for k in range(0, num):
    temp = text[0].split(' ')
    del[text[0]]
    a = int(temp[0])
    b = int(temp[1])

    count = 0
    
    for i in range(a, b+1):
        res = isPalindrome(i)
        s = math.sqrt(i)
        res2 = isPalindrome(s)

        if res and res2:
            count += 1

    o.write("Case #" + str(k+1) + ": " + str(count) + "\n")

o.close()

    

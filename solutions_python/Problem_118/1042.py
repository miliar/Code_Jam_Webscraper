import re, math

def palindrome(string):
    if len(string) > 3:
        return ( string[0] == string[-1] ) and palindrome(string[1:-2])
    else:
        return string[0] == string[-1]

def fair_and_square(count):
    bounds = raw_input()
    pal_count = 0
    a,b = bounds.split(' ')
    a = int(a)
    b = int(b)
    for i in range(a, b+1):
        if palindrome(str(i)):
            if math.pow(int(math.sqrt(i)), 2) == i and palindrome(str(int(math.sqrt(i)))):
                pal_count += 1
    print "Case #{}: {}".format(count, pal_count)

count = input()
for i in range(1, count+1):
    fair_and_square(i)

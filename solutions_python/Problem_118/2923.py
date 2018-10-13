import math
#a is a string
def isPalindrome(a):
    return str(a) == str(a)[::-1]
#a is a string
def squareisPalindrome(a):
    if int(math.sqrt(int(a)))==float(math.sqrt(int(a))):
        return isPalindrome(str(int(math.sqrt(int(a)))))
    return 0

#check range
def checkRange(rrr):
    count=0
    for number in rrr:
        if squareisPalindrome(number) and isPalindrome(number):
            count+=1
    return count

#read file and see how big list is
file=open("C-small-attempt2.in").readlines()[1:]

x=1
ranges=[]
#run through all the lines and make ranges
for numbers in file:
    ranges.append( range( int( numbers.split()[0] ), int( numbers.split()[1] ) + 1 ) )
things=[]
for ranger in ranges:
        things.append(checkRange(ranger))
x=1
for number in things:
    print("Case #"+str(x)+": "+str(number))
    x+=1
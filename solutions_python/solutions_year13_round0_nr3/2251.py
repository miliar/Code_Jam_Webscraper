from math import ceil, floor

def is_palindrome(num):
    number = str(num)
    size = len(number)
    i = 0
    while i < (size/2):
        if number[i] != number[size-i-1]:
            return False
        i += 1  
    return True

def read_input(filename):
    f = open(filename)
    tests = int(f.readline())
    for test in xrange(tests):
        limits = f.readline().split()
        yield(test+1, [int(ceil(int(limits[0])**.5)), 
                       int(floor(int(limits[1])**.5))])

myinput = read_input('C-small-attempt0.in')
output_file = open('Fair-and-square.out', "w")

for i in myinput:
    total = 0
    for number in xrange(i[1][0], i[1][1]+1):
        if is_palindrome(number) and is_palindrome(number**2):
            total += 1
    output_file.write("Case #%d: %d\n" % (i[0], total))

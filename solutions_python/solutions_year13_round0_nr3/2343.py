import math
def output(lines):
    for x, value in enumerate(lines):
        print ('Case #{0}: {1}'.format(int(x+1), value))

def palindrome(num):
    return int(str(num)[::-1]) == num

with open('input.txt', 'r') as f:
    cases=[]
    numlines = int(f.readline())
    for case in xrange(1,numlines+1):
        range = f.readline().rsplit(' ',1)
        fairAndSquare = 0
        if range:
           for x in xrange(int(range[0]), int(range[1])+1):
                root = int(math.sqrt(int(x)))
                if( palindrome(x)  and int(root + 0.5) ** 2 == int(x) and palindrome(root)):
                    fairAndSquare += 1
        cases.append(fairAndSquare)
output(cases)


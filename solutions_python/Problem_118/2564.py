from pylab import *

f = open("C-small-attempt0.in", "r")

a = 1
b = 1000000000

def isPalindrome(i):
    if len(i) < 2:
        return True
    first = i[0]
    last = i[-1]
    if first == last:
        return isPalindrome(i[1:-1])
    else:
        return False

def main(a,b):
    counter = 0
    for i in range(int(ceil(sqrt(a))), int(sqrt(b)) + 1):
        if isPalindrome(str(i)) and isPalindrome(str(i**2)):
            counter += 1
    return counter

if __name__ == '__main__':
    #print main(a,b)
    t = int(f.readline())
    for case in range(1, t+1):
        inp = f.readline().split()
        a = int(inp[0])
        b = int(inp[1])
        count = main(a,b)
        print "Case #%i: %i" %(case, count)

import math
class Interval:
    def __init__(self, rangeList):
        self.interval = rangeList
    
    def isPalindrome(self, num):
        palindrome = str(num)
        inverse = palindrome[::-1]
        return palindrome == inverse
    
    def isSquare(self, num):
        root = math.sqrt(num)
        x = int(root)
        return root == x
    
    def isFairSquare(self, num):
        if self.isPalindrome(num):
            if self.isSquare(num):
                return self.isPalindrome(long(math.sqrt(num)))
        return False
    
    def count(self, length):
        acum = 0
        for i in self.interval:
            if self.isFairSquare(i):
                acum += 1
        return acum
    
if __name__ == '__main__':
    fi = open("C-small-attempt0.in")
    text = fi.read()
    token = text.split()
    cases = long(token[0])
    del token[0]
    lists = 1
    count = 0
    for i in range(cases):
        firstEndPoint = long(token[0])
        del token[0]
        secondEndPoint = long(token[0])+1
        del token[0]
        while secondEndPoint - firstEndPoint > 50000000:
            midPoint = firstEndPoint + 50000001
            interval = Interval(range(firstEndPoint, midPoint))
            count += interval.count(len(interval.interval))
            firstEndPoint += 50000000
        interval = Interval(range(firstEndPoint, secondEndPoint))
        count += interval.count(len(interval.interval))
        print "Case #" + str(i+1) + ": " + str(count)
        count = 0
    pass
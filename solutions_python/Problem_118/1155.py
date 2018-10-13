def numFairSquare(start, end):
    s = int(start ** 0.5)
    e = int(end ** 0.5)

    num = 0

    for i in range(s, e + 1):
        if isPalindrome(i) and isPalindrome(i ** 2):
            if i ** 2 >= start and i **2 <= end:
                num += 1
    return num

def isPalindrome(n):
    s = list(str(n))
    r = s[:]
    r.reverse()
    return s == r

if __name__ == '__main__':
    num = int(raw_input())
    for i in range(num):
        (start, end) = map(int, raw_input().split())
        print 'Case #%d: %d' % (i + 1, numFairSquare(start, end))

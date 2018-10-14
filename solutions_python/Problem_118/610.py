
def isPalindrome(num):
    s = str(num)
    for i in range(len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def binSearch(p, num):
    lo = 0
    hi = len(p)
    while lo < hi:
        mid = (lo+hi)/2
        if p[mid] == num:
            return mid
        if p[mid] > num:
            hi = mid
        if p[mid] < num:
            lo = mid + 1
    return mid

p = []
for i in range(1,10000001):
    if isPalindrome(i):
        if isPalindrome(i*i):
            p.append(i*i)

cases = int(raw_input())
for i in range(1,cases+1):
    a, b = map(int,raw_input().split())
    print "Case #"+str(i)+": "+str(sum([1 for num in p if num >= a and num <= b]))

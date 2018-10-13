import math
def chequepalindrome(a):
    a = str(a)
    length = len(a)
    for i in range(length):
        if i >= length - 1 - i:
            break
        if a[i] != a[length - i - 1]:
            return False
    return True

t = int(raw_input())
for x in range(t):
    count = 0
    inp = raw_input()
    a,b = inp.split(' ')
    a = int(a)
    b = int(b)
    a = math.sqrt(a)
    sb = int(math.sqrt(b))
    sa = int(a)
    sb += 1
    if not a.is_integer():
        sa += 1
    for k in range(sa,sb):
        if chequepalindrome(a = k) and chequepalindrome(a = (k*k)):
            count += 1
    print 'Case #%s: %s' %(str(x+1),str(count))

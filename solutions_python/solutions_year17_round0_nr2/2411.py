



def findTidyNumber(n):
    num = list(str(n))
    if len(num) == 1: return n

    i = 0
    while i < len(num)-1:
        if num[i] > num[i+1]:
            while i > 0 and num[i-1] == num[i]: i -= 1
            num[i] = str(int(num[i])-1)
            break
        else: i += 1
    for k in range(i+1,len(num)):
        num[k] = '9'
    return int(''.join(num))

t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    print ("Case #%d: %d" %(i,findTidyNumber(n)))


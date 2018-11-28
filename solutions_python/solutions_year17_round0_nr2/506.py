N = int(input())
for n in range(N):
    m = int(input())
    target = 0
    
    rev = [c for c in str(m)]
    out = ['0'] * len(rev)
    for i in range(len(rev)-1):
        if ord(rev[i]) > ord(rev[i+1]):
            rev[i] = chr(ord(rev[i])-1)
            for j in range(i+1, len(rev)):
                rev[j] = '9'
            break
    for i in range(len(rev)-1,0,-1):
        if ord(rev[i]) < ord(rev[i-1]):
            rev[i-1] = chr(ord(rev[i-1])-1)
            rev[i] = '9'

    target = 0
    for c in rev:
        target *= 10
        target += ord(c) - ord('0')
    print("Case #", n+1, ": ", (target), sep="")
   
"""
    while m > 0:
        target *= 10
        if m % 10 >= (m//10) %10 and not (m%10==0 and m != 0):
            target += m % 10
#            print(m%10, m)
        else:
            target += 9
            m -= 10
#           print(9, m)
        m //= 10

    print("Case #", n+1, ": ", str(target)[::-1], sep="")
    """

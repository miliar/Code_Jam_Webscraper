from math import sqrt
f = open("input.txt","r")
t = int(f.readline())
out = open("output.txt","w")
def palindrome(n):
    z = str(n)
    le = len(z)
    if le == 1:
        return True
    mid = le/2
    if le&1 == 1:
        up = mid + 1
    else:
        up = le/2
    if z[:mid] == z[up:][::-1]:
        return True
    else:
        return False
    
for a in xrange(t):
    x,y = map(int,f.readline().split())
    count = 0
    for i in xrange(x,y+1):
        sqr = sqrt(i)
        if int(sqr) == sqr and palindrome(i) == True:
            if palindrome(int(sqr)) == True:
                count += 1
    wr = "Case #" + str(a+1) + ": " + str(count) + '\n'
    out.write(wr)
f.close()
out.close()
            

#Palindrome procedure -- check
def iter_palindrome(s):
    s = str(s)
    for i in range(0, len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True
    
hand = open('C-small-attempt0.in') # based on the downloaded file
count = 0
for line in hand:
    m = line.split()
    if len(m) > 1:
        count += 1
        a = int(m[0])
        b = int(m[1])
        res = 0
        for n in range(a,b+1):
            if iter_palindrome(n) and n**0.5==int(n**0.5) and iter_palindrome(int(n**0.5)):
                res += 1
        print "Case #%d: %d" %(count,res)
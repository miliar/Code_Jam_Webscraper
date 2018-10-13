
def is_tidy(n):
    digit = n%10
    while n > 0:
        if n % 10 > digit:
            return False
        digit = n % 10 
        n = n // 10
        
    return True

def pr(n):
    while not is_tidy(n):
        n = n - 1
    return n

t = raw_input()
for i in range(int(t)):
    n = int(raw_input())
    n = pr(n)
    print "Case #" + str(i+1) + ": " + str(n)


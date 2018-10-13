def isPalindrome(x):
    x = str(x)
    if x==x[::-1]:
        return True
    return False

def initialize():
    x = []
    for i in xrange(1,32):
        if(isPalindrome(i) and isPalindrome(i*i)):
            x+=[i*i]
    return x

ip = open("input.txt", "r")
op = open("output.txt", "w")
x = initialize()
t = int(ip.readline())
for _ in xrange(t):
    start, end = map(int, ip.readline().strip().split())
    count = 0
    for i in x:
        if i>=start and i<=end:
            count+=1
    op.write("Case #"+str(_+1)+": "+str(count)+"\n")
ip.close()
op.close()

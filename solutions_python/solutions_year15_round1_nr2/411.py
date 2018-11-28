import sys

input = file(sys.argv[1]).readline

def gcd(a,b):
    if b == 1:
        return 1
    if a==b or b==0:
        return a
    if a<b:
        return gcd(b,a)
    return gcd(a%b,b)
def getMin(x):
    number = 0
    n = 1
    for i in x:
        n = n*i/gcd(n,i)
    for i in x:
        number += n/i
    return n, number

def solution(n, x, y):
    Min, number = getMin(y)
    x = x%number
    if x == 0:
        x = number
    if x <= n and x!=0:
        return x
    time = min(y)
    x -= n
    while True:
        ans = 0
        for i in y:
            ans += time/i
        if ans >= x:
            count = ans-x
            for i in xrange(n):
                if time%y[n-1-i]==0:
                    if count == 0:
                        return n-i
                    count -= 1
        time += 1    

for case in range(int(input())):
	x = [int(num) for num in input().strip().split(' ')]
	y = [int(num) for num in input().strip().split(' ')]
	print "Case #%d: %d " % (case+1, int(solution(x[0],x[1],y)))

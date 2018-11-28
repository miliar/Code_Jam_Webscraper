import sys

last_number = 0
sys.setrecursionlimit(2000)

def func(n,k):
    if k<=1:
        mx = int(n/2)
        mi = int(n/2-(n+1)%2)
        return (mx,mi)
    elif k>=n:
        return (0,0)
    elif n%2==0:
        return func(int((n/2)-k%2),int(k/2))
    else:
        return func(int((n/2)),int(k/2))

input = open('gs3.txt', 'r')
tests = int(input.readline())
# print (tests)
for i in range(1,tests+1):
    test = input.readline()
    (n,k) = test.split(' ')

    (mx,mi)=func(int(n),int(k))
    print ('Case #%s:'%i,mx,mi)

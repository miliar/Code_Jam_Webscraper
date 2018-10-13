import math
def pal(L):
    LL = str(L)
    return LL == LL[::-1]

def square(n):
    return math.sqrt(n).is_integer()

def calc(A,B):
    c = 0
    for n in range(A,B+1):
        if pal(n) and square(n):
            if pal(int(math.sqrt(n))):
#                print(n)
                c = c + 1
    print('Case #' + str(TC+1) + ": " + str(c))
global TC
p1 = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L, 100000020000001L]
f = open('C-large-1.in','r')
T = f.readline()
T = int(T[0:-1])
for TC in range(0,T):
    CC = f.readline()
    [A,B] = CC.split()
    A = int(A)
    B= int(B)
    count = 0
    for g in p1:
        if g >= A and g <= B:
            count = count+1
    print('Case #' + str(TC+1) + ": " + str(count))

# trying to reverse engineer palindromes
#maxB = 10**14
#maxsqB = int(math.sqrt(maxB)) + 1

#pl = []
#for x in range(1,maxsqB+1):
#    if pal(x):
#        sx = x**2
#        if pal(sx):
#            print(sx)
#            pl.append(sx)
            


def is_palin(n):
    s = str(n)
    l = len(s)
    for i in xrange(l/2):
        if s[i] != s[l-1-i]:
            return False
    return True

def rev(n):
    r = 0
    while n > 0:
        r = r*10 + n %10 # r *= 10
        n /= 10
    return r

palins = []
fas = []

def add_fas(n):
    a = n*n
    if is_palin(a):
        fas.append(a)

for i in range(1, 7):
    j = 10 ** (i-1)
    J = j * 10 - 1
    
    while j <= J:
        p1 = j * (10 ** (i-1)) + rev(j/10)
        p2 = j * (10 ** (i)) + rev(j)
        
        add_fas(p1)
        add_fas(p2)
        
        j += 1

'''
while i <= 10**50 + 1:
    if is_palin(i):
        palins.append(i)
    i += 1
    10^1
    10^1
    10^2  # 3
    10^2  # 4
    10^3  # 5
    10^3  # 6 
    10^25 # 49
    10^25 # 50
''' 

T = input()
for case in xrange(1, T+1):
    A, B = map(long, raw_input().split())
    
    #Ar = 1 # long(B**0.5)
    #Br = long(B**0.5)+1
    #i = Ar
    
    #    i += 1 
    c = 0
    for f in fas:
        if A <= f and f <= B:
            c += 1
    print 'Case #%d: %d' % (case, c)
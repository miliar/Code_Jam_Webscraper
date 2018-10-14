import time


def is_palin(n):
    s = str(n)
    l = len(s)
    for i in xrange(l/2):
        if s[i] != s[l-1-i]:
            return False
    return True
   
palins = []
fas = []

i = long(1)
while i <= 10**7 + 1:
    if is_palin(i):
        palins.append(i)
    i += 1
    
for palin in palins:
    a = palin*palin 
    if is_palin(a):
        fas.append(a)

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
import math

def get_a_b(s):
    l = s.split(' ')
    a = int(l[0])
    b = int(l[1])
    return a,b

def is_palindrome(n):
    s1 = str(n)
    s2 = s1[::-1]
    return (s1 == s2)

def is_square(n):
    rr = math.sqrt(n)
    r = int(rr)
    return (rr == r) and (is_palindrome(r))

fi = open("C-small-attempt0.in", 'r')
fo = open("C-small.out", 'w')

t = int(fi.readline())
cache = []

for i in range(t):
    a,b = get_a_b(fi.readline())
    count = 0
    j = a - 1
    while j < b:
        j = j + 1
        if j in cache:
            count = count + 1
        elif is_palindrome(j) and is_square(j):
            cache.append(j)
            #print j
            count = count + 1

    fo.write("Case #%s: %s\n" % (i+1, count))

fi.close()
fo.close()

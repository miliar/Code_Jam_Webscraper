import math as m
def palindrome(x):
    s = "%d"%x
    return s == s[::-1]

def palindromes(a,b):
    # astr = map(lambda x:x, "%d"%a)
    # alen = len(astr)
    # for i in range(alen/2):
    #     astr[-(i+1)] = astr[i]
    # # astr is now a palindrome and the smallest palindrome which is at least a
    # a = int(''.join(astr))
    while not palindrome(a):
        a = a + 1

    while a <= b:
        yield int(a)
        a = a + 1
        while not palindrome(a):
            a = a + 1

    

T = int(raw_input(''))
for t in range(T):
    A,B = map(int, raw_input('').split(' '))

#    print A, ",", B

    count = 0
    # Search for palindromes which can be squared into palindromes

    for x in palindromes(int(m.ceil(m.sqrt(A))),int(m.floor(m.sqrt(B)))):
        if x*x > B:
            break
        if palindrome(x*x):
#            print x, x*x
            count = count+1

    # for x in  range(A,B+1):
    #     if palindrome(x):
    #         sqrx = int(m.sqrt(x))
    #         if x == sqrx*sqrx:
    #             if palindrome(sqrx):
    #                 print sqrx, x
    #                 count = count+1
                    
    print ("Case #%d:"%(t+1)), count

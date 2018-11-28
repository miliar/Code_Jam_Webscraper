from math import sqrt, ceil

def palindrome(n):
    temp = n
    p = 0
    while(temp != 0):
        p = 10*p + temp % 10
        t = temp%10
        if(t > 3):
            return False
        temp = temp/10
    if(n == p):
        return True
    return False

def palindrome_square(n):
    temp = n
    p = 0
    while(temp != 0):
        p = 10*p + temp % 10
        temp = temp/10
    if(n == p):
        return True
    return False


def fareAndSquare(n1, n2):    
    counter = 0
    r_min = int(ceil(sqrt(n1)))
    r_max = int(sqrt(n2))
    #print "range: ", r_min, r_max
    i = r_min
    while(i <= r_max):
        #check if square of r is a palindrome
        if(palindrome(i)):
            if(palindrome_square(i**2)):
                counter = counter + 1
                #print i, i**2
        i = i + 1
    return counter

fin = open("C-small-attempt2.in", "r")
fout = open("output", "w")

T = eval(fin.readline())
 
l = []

for i in range(T):
    c = fin.readline()
    cr = c.split(' ')
    r_min = eval(cr[0])
    r_max = eval(cr[1])
    fout.write("Case #{0}: {1}\n" .format((i+1), fareAndSquare(r_min, r_max)))

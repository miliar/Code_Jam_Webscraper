f = open('C:/Users/vtrinh/Downloads/C-small-attempt0.in', 'r')
o = open('C:/Users/vtrinh/Downloads/C-small-attempt0.out', 'w')

T = int(f.readline().strip())

def isqrt(x):
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def isPalindrome(word):
    return word == word[::-1]

for t in range(0, T, 1):

    # Read A B
    line = f.readline().strip().split(' ')
    A, B = int(line[0]), float(line[1])

    count = 0
    for i in range(A, int(B)+1, 1):
        if isPalindrome(str(i)):
            j = isqrt(i)
            if i == j**2:
                if isPalindrome(str(j)):
                    count +=1

    res = str(count)
    s = "Case #%d: %s\n" % (t+1, res)
    print(s)
    o.write(s)
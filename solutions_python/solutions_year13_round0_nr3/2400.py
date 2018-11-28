
import math

def is_square(n):
    return math.sqrt(n).is_integer()

def is_palindrome(n):
    a = int(math.log10(n))

    j = 0
    for i in range(a,a//2,-1):
        if n//math.pow(10,i)%10 != n//math.pow(10,j)%10:
            return False
        j = j+1

    return True

inf = open("in.txt")
outf = open("out.txt",'w')

noc = int(inf.readline())

count = 0
for i in range(noc):
    start,end = inf.readline().split()
    start = int(start)
    end = int(end)

    count = 0
    for j in range(start, end+1):
        if is_palindrome(j) and is_square(j) and is_palindrome(math.sqrt(j)):
            count = count+1

    outf.write("Case #%d: %d\n" % (i+1, count))

inf.close()
outf.close()

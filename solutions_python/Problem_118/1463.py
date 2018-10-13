import fileinput,sys
import math

print_indicator = 0

def myprint(*arg):
    if print_indicator != 0:
        print print_indicator
        print arg

lines = []

for line in fileinput.input():
    lines.append(line)

n= int(lines[0])

def int_root(val):
    root = math.sqrt(val)
    return (float(int(root)) == root)

def palindrome(val):
    s=str(val)
    last = len(s)-1
    first = 0
    result = True
    #myprint ("s,val,first,last",s,val,first,last)
    while (last > first):
        if (s[first] != s[last]):
            result = False
            break;
        last-=1
        first+=1
    if result:
        pass
        #print s
    return result 

def slow(A,B):
    myprint("A,B", A,B)
    fair = 0
    for i in xrange(A,B+1):
        if (palindrome(i) and int_root(i) and palindrome(int(math.sqrt(i)))):
            fair+=1
    return fair

def bit_faster(A,B):
    f = int(math.sqrt(A))
    g = int(math.sqrt(B)+.5)
    fair = 0
    for i in xrange(f,g+1):
        if (i*i >= A and i*i <= B):
            val = i*i
            if (palindrome(i) and palindrome(val)):
                fair+=1
    return fair

def make_palindromes(s):
    result1 = s
    result2 = s
    for x in xrange(len(s)-1,-1,-1):
        result1 += s[x]
    for x in xrange(len(s)-2,-1,-1):
        result2 += s[x]
    return (result1, result2)
    

def faster_still(A,B):
    d = max(int(math.log(A,2))/4-4,0)
    d1 = int(math.log(B,2))/4+4 
    count = 0
    for val in xrange(2**d-1,2**(d1+1)):
        pattern = str(val)
        (pat1,pat2) = make_palindromes(pattern)
        myprint("val, patterns", val,pat1,pat2)
        val1 = int(pat1)
        sq1 = val1*val1
        val2 = int(pat2)
        sq2 = val2*val2
        if (sq1 >= A and sq1 <= B and palindrome(sq1)):
            count+= 1
        if (sq2 >= A and sq2 <= B and palindrome(sq2)):
            count+= 1
    myprint("Count", count)
    return count
            
case = 0
line_no =1      
for j in xrange(1,n+1):
    board = []
    case +=1
    print "Case #%d:" % (case),
    nbym = (lines[line_no]).partition(" ")
    A = int(nbym[0])
    B = int(nbym[2])
    myprint("A,B", A,B)
    fair = 0
    print slow(A,B)
    #print bit_faster(A,B)
    #print faster_still(A,B)
    line_no+=1

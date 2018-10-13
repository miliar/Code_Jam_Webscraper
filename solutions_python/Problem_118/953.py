import bisect
import math

fin = open("C-large-1.in")
fout = open("prob3.out", "w")

def isPalindrome(number):
    s = str(number)
    return s == s[::-1]

palindromes = [x for x in xrange(10**7) if isPalindrome(x)]

num_cases = int(fin.readline())
for case_number in xrange(num_cases):
    a, b = map(int, fin.readline().split())
    start = bisect.bisect_left(palindromes, math.ceil(math.sqrt(a)))
    end = bisect.bisect_right(palindromes, math.floor(math.sqrt(b)))

    #print palindromes[start:end]
    count = 0
    for x in palindromes[start:end]:
        sq = x**2
        if  isPalindrome(sq): 
            count += 1
    
    #print "Case #%d: %s\n" % (case_number+1, count)
    fout.write("Case #%d: %s\n" % (case_number+1, count))
    
fout.close()

from math import sqrt, log10

def int_reverse(n):
    result = 0
    while n > 0:
        result *= 10
        result += n%10
        n /= 10
    return result

def is_fair(n):
    return n == int_reverse(n)


"""
def is_fair(n):
        nb_digit = int(log10(n))
        left_digit_divisor = 10**nb_digit
        
        for i in range(nb_digit/2 + nb_digit%2):
            if n%10 != n/left_digit_divisor:
                return False
            n/= 10
            left_digit_divisor /= 100
        return True
"""

def palindromes(length):
   "a generator of all palindrome of some length"
   if length == 1:
      for i in xrange(10):
          yield i
   elif length == 2:
       for i in xrange(10):
          yield i*11
   else:
       left_digit_mul = 10**(length-1)
       for i in xrange(1,10):
           for j in palindromes(length-2):
              yield i*left_digit_mul + j*10 +i

def palindromes_range(a,b):
    "a generator of all palindromes >=a and <=b"
    lena = int(log10(a))+1
    lenb = int(log10(b))+1
    for i in xrange(lena, lenb+1):
        for j in palindromes(i):
            if a<=j<=b:
               yield j
            if j > b:
               break
    
def count_fair_square(a,b):
    count = 0
    min_search = int(sqrt(a))
    if min_search*min_search < a:
       min_search +=1
    max_search = int(sqrt(b))
    for i in palindromes_range(min_search, max_search):
        if is_fair(i*i):
            count += 1
    return count

   
    
n_test_case = input()
for i in xrange(1, n_test_case+1):
    a,b = raw_input().split()
    a = int(a)
    b = int(b)
    print 'Case #%d: %d' % (i, count_fair_square(a,b))


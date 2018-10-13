import math

def decompo(n): # The number will be spelled backwards, but doesn't matter for a palidrome-checking
    l = []
    while n != 0:
        l.append(n % 10)
        n /= 10
    return l

def is_palindrome(n):
    l = decompo(n)
    return l == list(reversed(l))

def is_perfect_square(n):
    return math.sqrt(n) == math.trunc(math.sqrt(n))

def is_fair_square(n):
    return is_perfect_square(n) and is_palindrome(n) and is_palindrome(int(math.sqrt(n)))

if __name__ == '__main__':
    n = int(raw_input())
    l = [map(lambda x : int(x), raw_input().split()) for _ in range(n)]
    
    for i in range(n):
        a, b = l[i]
        count = 0
        
        for j in range(a, b + 1):
            if is_fair_square(j):
                count += 1
        
        print "Case #%d: %d" % (i + 1, count)

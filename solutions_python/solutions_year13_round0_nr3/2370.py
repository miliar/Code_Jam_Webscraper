import math

def is_palindrome(word):
    return word == word[::-1]

for i in range(int(raw_input())):
    a, b = map(int, raw_input().split())
    count = 0
    for n in range(a, b + 1):
        sr = int(math.sqrt(n))
        if sr * sr != n:
            continue
        if not is_palindrome(str(n)):
            continue
        if not is_palindrome(str(sr)):
            continue
        #print '{}, {}'.format(n, sr) 
        count += 1
    print 'Case #{}: {}'.format(i + 1, count)

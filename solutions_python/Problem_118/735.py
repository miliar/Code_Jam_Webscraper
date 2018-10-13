import math

def is_pal(n):
    s = list(str(n))
    N = len(s)
    for i in xrange(N/2):
        if s[i] != s[N-1-i]:
            return False
    return True

def isqrt(n):
    x = int(2**(math.ceil((1+math.floor(math.log(n)/math.log(2)))/2.0)))
    while True:
        y = (x+n/x)/2
        if y >= x:
            return x
        x = y

def palindromes_from(A):
    # Construct generating half for palindrome.
    # For current half, generate palindrome, yield and update.
    def complete(half, phase):
        word = str(half)
        return int(word + word[(-2 if phase==0 else -1)::-1])
    # N: length of the palindrome.
    sA = str(A)
    N = len(sA)
    phase = 1 - (N % 2)
    half_len = (N+1)/2
    half = int(sA[:half_len])
    bound = 10**half_len

    if complete(half,phase) < A:
        half += 1
        if half == bound:
            if phase == 0:
                half = half/10
                phase = 1
            else:
                phase = 0
                bound *= 10

    # ph: the phase of completion.
    # bound: the bound for phase change.
    while True:
        yield complete(half,phase)
        half += 1
        if half == bound:
            if phase == 0:
                half = half/10
                phase = 1
            else:
                phase = 0
                bound *= 10

def count_fair_squares(A,B):
    a = isqrt(A)
    if a*a < A:
        a += 1
    b = isqrt(B)
    #print "For ",A,B,"effective bounds are ",a,b,"."
    # At this point, we are searching in [a,b]
    count = 0
    for p in palindromes_from(a):
        #print "Trying pal ",p,"..."
        if p > b:
            #print "Hit border... quitting."
            break
        sq = p*p
        #print "Pal square is",sq,"..."
        if is_pal(sq):
            count += 1
            #print "Hit!, count is",count
    return count



def tests():
    assert is_pal(1)
    assert is_pal(121)
    assert not is_pal(133)
    assert is_pal(91133119)
    assert isqrt(1) == 1
    assert isqrt(3) == 1
    assert isqrt(4) == 2
    assert isqrt(5) == 2
    assert isqrt(10**18+1) == 10**9
    assert count_fair_squares(1,4) == 2
    assert count_fair_squares(10,120) == 0
    assert count_fair_squares(100,1000) == 2
    print "Tests pass"


# Actual solve
def solve():
    T = int(raw_input())
    for t in xrange(T):
        A,B = map(int,raw_input().split())
        print "Case #" + str(t+1) + ":",count_fair_squares(A,B)

solve()

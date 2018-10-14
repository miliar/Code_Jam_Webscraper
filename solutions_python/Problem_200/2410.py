import fileinput

def tidynum(n):
    scale = 10**6
    if n < scale:
        return tidynum_naive(n)
    else:
        n1 = n % scale
        n //= scale
        n2 = n % scale
        n //= scale
        n3 = n % scale
        n4 = n // scale
        if n4 == 1: 
            return (10**15 - 1)
        else:
            n3_new = tidynum_naive(n3)
            n2_new = tidynum_naive(n2)
            n1_new = tidynum_naive(n1)
            n3_lo = n3_new % 10
            n2_hi = n2_new // (10**5)
            n2_lo = n2_new % 10
            n1_hi = n1_new // (10**5)
            if (n1_hi < n2_lo):
                n2_new = tidynum_naive(n2_new-1)
                n1_new = scale - 1
                n2_hi = n2_new // (10**5)

            if (n2_hi < n3_lo):
                n3_new = tidynum_naive(n3_new-1)
                n2_new = scale - 1
                n1_new = scale - 1

            ret = (n3_new * scale + n2_new) * scale + n1_new
            return ret

def tidynum_naive(n):
    #assumes that n is smaller than 1000000
    while (not in_order(n)):
        n -= 1
    return n

def in_order(number,prev = 10):
    new = number % 10
    if(number == 0):
        return True
    elif (new > prev):
        return False
    else:
        return in_order(number//10,new)

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input()) # read a list of integers
  print("Case #{}: {}".format(i,tidynum(n)))
  # check out .format's specification for more formatting options

debug_mode = False

def debug(*args):
    if debug_mode:
        print("DEBUG: ", end='')
        print(*args)

def is_tidy(n):
    last = 0
    for d in str(n):
        if int(d) < last:
            return False
        last = int(d)
    return True

# For any given number that starts 'x' the FIRST tidy number starting 'x' is all x's and 
# the last tidy number before is x000... - 1. If we're higher than the first tidy number 
# for a set of digits we can ignore the first digit (as the second is clearly higher) and 
# do the same check internally. 

def find_tidy(n):
    debug("Find", n)
    if is_tidy(n):
        return n
    s = str(n)
    first_digit = s[0]
    first_tidy = int(first_digit * len(s))
    if n < first_tidy:
        last_tidy = int(first_digit + ("0" * (len(s) - 1))) - 1
        debug("Less than first, use last", last_tidy)
        return last_tidy
    last_tidy = int(first_digit + str(find_tidy(int(s[1:]))))
    debug("After recursion answer is ", last_tidy)
    return last_tidy

t = int(input())
q = 1
while q <= t:
    a = str(find_tidy(int(input())))
    print("Case #{qno}: {ans}".format(qno=q, ans=a))
    q = q + 1

import math

fin= open("in.txt")
fout = open("out.txt", "w")

count = int(fin.readline())

LOWER = 0
UPPER = 0

def to_int_array(s):
    return [int(x) for x in s.split(' ')]


def find_palindrome_from(x):
    """
    given a number that may not be a palindrome, find the next highest
    number that is a palindrome.
    """
    while not is_palindrome(x):
        x = x+1

    return x



def find_next_palindrome(x):
    p = [int(c) for c in str(x)]

    def mod_inc(i):
        return (i + 1) % 10

    def array_to_int(arr):
       return int("".join([str(x) for x in arr]))

    result = []
    length = len(p)

    mid = int(math.ceil(length/2))
    next_ = mod_inc(p[mid])
    result.append(next_)


    # odd:
    if length % 2 == 1:
        mid = int(math.ceil(length/2))
        p[mid] = mod_inc(p[mid])

        offset = 0
        while p[mid+offset] == 0:
            offset = offset+1

            next_ = mod_inc(p[mid-offset])
            if mid-offset < 0:
                p.append(next_)
                p[0] = next_
                return array_to_int(p)
            else:
                p[mid-offset] = next_
                p[mid+offset] = next_

    # even:
    else:
        mid_h = int(length/2)
        mid_l = mid_h-1
        p[mid_h] = mod_inc(p[mid_l])
        p[mid_l] = p[mid_h]
        offset = 0
        while p[mid_h+offset] == 0:
            offset = offset+1

            if mid_l-offset < 0:
                p.append(1)
                p[0] = 1
                return array_to_int(p)
            next_ = mod_inc(p[mid_h+offset])
            p[mid_h+offset] = next_
            p[mid_l-offset] = next_

    return array_to_int(p)


def is_palindrome(x):
    sx = str(x)

    for i in range(int(math.ceil(len(sx)/2.0))):
        if sx[i] != sx[len(sx)-1-i]:
            return False

    return True


def count_fair_square(lower, upper):
    """
    Approach this backwards. Take sqrt(lower), find the next palindrome
    after it. Then keep finding next palindromes, until the square-root
    of the palindrome is greater than upper
    """
    count = 0
    x = int(math.ceil(math.sqrt(lower)))
    p = find_palindrome_from(x)
    p_squared = p**2
    while p_squared <= upper:
        if is_palindrome(p_squared):
            #print "## found: ", p_squared
            count = count + 1

        p = find_next_palindrome(p)
        p_squared = p**2

    return count


i=1
while i <= count:
    # read in one test case
    dimmension_line = fin.readline()
    lower, upper = to_int_array(dimmension_line)

    total = count_fair_square(lower,upper)
    s = "Case #{}: {}".format(i, total)
    print s
    fout.write(s + "\n")

    i = i+1


fin.close()
fout.close()

"""
known:
    1, 4, 9, 121, 484



"""

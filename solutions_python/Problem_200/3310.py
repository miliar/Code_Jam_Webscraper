
'''
Created on Apr 12, 2013

@author: herman
'''


infile = open("input.txt","r")
outfile = open("output.txt","w")

trials = int(infile.readline())

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def last_tidy(N):
    digits = [int(d) for d in list(str(N))]
    ndigits = len(digits)

    curr = 0
    decidx = None
    for i in xrange(ndigits):
        if digits[i] < curr:
            decidx = i
            break
        curr = digits[i]        
    
    if decidx is None:
        return N

    newdigits = digits
    newdigits[decidx-1] -= 1
    # need to check this doesn't break order
    while newdigits[decidx-1] < newdigits[decidx - 2] and decidx > 1:
        decidx -= 1
        newdigits[decidx-1] -= 1
    for i in xrange(decidx,ndigits):
        newdigits[i] = 9
    return int("".join([str(nd) for nd in newdigits]))

def count(tidy_num):
    digits = [int(d) for d in list(str(tidy_num))]
    ndigits = len(digits)
    # single digits special case
    # if ndigits == 1:
    # return tidy_num
    
    ntidy = 0
    didx = 0
    dleft = ndigits - 1
    curr_value = 0
    # this doesn't count the last tidy number, but counts 0
    while dleft > 0:
        dividers = 10-curr_value-1
        ntidy += choose(dividers+dleft,dividers)
        # update place in number
        if curr_value < digits[didx]:
            curr_value += 1
        while curr_value == digits[didx] and dleft > 0:
            didx += 1
            dleft -= 1

    # single digit contribution
    ntidy += digits[didx] - curr_value    
    return ntidy
    

for i in xrange(trials):
    N = int(infile.readline())

    s = "Case #%d: %d\n" % (i+1,last_tidy(N))
    outfile.write(s)
    print s
    
infile.close()
outfile.close()

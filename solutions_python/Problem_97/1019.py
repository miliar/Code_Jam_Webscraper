import sys

def recycled_count(a,b,num):
    digits = str(num)
    count=0
    #possible_permutations = set([int(digits[i:]+digits[:i]) for i in range(1,len(digits))])
    #for i in possible_permutations:
    #    if i > num and i<=b:
    #        count+=1
    for i in range(1,len(digits)):
        p_digits = digits[i:]+digits[:i]
        if not p_digits==digits:
            p = int(p_digits)
            if p > num and p <= b:
                count+=1
    return count
    #return filter(lambda (x,n):n!=num and n>=a and n<=b,possibilities)
        

def process_line(line):
    parts = [int(x) for x in line.split(" ")]
    a = parts.pop(0)
    b = parts.pop(0)

    nums = xrange(a,b+1)
    result = 0
    for i in nums:
        count = recycled_count(a,b,i)
        result += count
    result = result
    return result 


inputfile='C-small-attempt0.in'
input = [line.strip() for line in open(inputfile).readlines()]

t = int(input.pop(0))

for i in range(t):
    #print input[i]
    print "Case #%i: %i" % (i+1,process_line(input[i]))
    sys.stdout.flush()

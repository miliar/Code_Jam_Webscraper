

def larger_one_digits(n):
    return any([int(i) for i in str(n) if int(i) > 1])

def is_tidy(n):
    l = [int(i) for i in str(n)]
    return all(x<=y for x,y in zip(l,l[1:]))

def digits_to_number(digits):
    return reduce(lambda x, y : x + y, map(str, digits))

def last_tidy(n):
    if n <= 1000 or larger_one_digits(n):
        found = 0
        while found == 0:
            if is_tidy(n):
                found = 1
            else:
                n -= 1
    else:
        n = digits_to_number([9]*(len(str(l))-1))
    return n

with open('B-small-attempt1.in','r') as fin, open('tidy_sm.out','w') as fout:
    for i, l in enumerate(fin):
        if (i > 0):
            fout.write('Case #%d: %s\n' % (i, last_tidy(int(l))))
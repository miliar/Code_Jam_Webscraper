def process(n):
    s = str(n)
    s = list(s)
    i = len(s) - 1
    while i > 0:
        if i > 0:
            if int(s[i]) < int(s[i - 1]):
                c = int(s[i - 1])
                c = c -1
                s[i - 1] = str(c)
                j = i
                while j < len(s):
                    s[j] = '9'
                    j = j + 1             
                s = ''.join(s)
                return int(s)
        i = i - 1
    s = ''.join(s)
    return int(s)
                

def validate(n):
    s = str(n)    
    s_sorted = ''.join(sorted(s))
    if s == s_sorted:
        return True
    else:
        return False
    
def get_tidy_number(s):
    n = int(s)
    while n > 0:
        n = process(n)
        if validate(n):
            return n
        n = n - 1
       
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = get_tidy_number(raw_input())    
    print "Case #{}: {}".format(i, n)
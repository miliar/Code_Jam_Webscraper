def process_zero(n):
    s = str(n)    
    while s.find('0') != -1 and s.index('0') != 0:
        i = s.rfind('0')
        list_s = list(s)
        c = int(list_s[i-1])
        if c > 0:
            c = c - 1
        else:
            c = 9
        list_s[i-1] = str(c)        
        while i < len(s):
            list_s[i] = '9'
            i = i + 1
        s = ''.join(list_s)        
    return int(s)

def validate(n):
    s = str(n)    
    s1 = ''.join(sorted(s))
    if s == s1:
        return True
    else:
        return False
    
def tidy(s):
    n = int(s)
    while n > 0:
        #n = process_zero(n)
        if validate(n):
            return n
        n = n - 1
       
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = tidy(raw_input())    
    print "Case #{}: {}".format(i, n)
  # check out .format's specification for more formatting options
import sys
filename = sys.argv[0] 

result = ''
_in = open(filename.replace('.py', '.in'), 'r').read().splitlines()
_in.pop(0)


def isPal(n):
    r = list(str(n))
    r.reverse()
    return str(n) == ''.join(r)    

def isSqrt(n):
    s = n**0.5
    if s % 1 == 0 and isPal(int(s)):
        return True 
    return False   


for idx, pair in enumerate(_in):
    p = map(int, pair.split(' '))
    count = 0
    for j in xrange(p[0], p[1]+1):
        if isSqrt(j) and isPal(j):
            count += 1
    result +=  'Case #%s: %d\n' % (idx+1, count)

_out = open(filename.replace('.py', '.out'), 'w')
_out.write(result)
_out.close()


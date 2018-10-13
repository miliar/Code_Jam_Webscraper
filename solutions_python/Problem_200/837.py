import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
lines = [x for x in lines if len(x) > 0]

def is_tidy(s):
    last_c = '0'
    for c in s:
        if c < last_c:
            return False
        last_c = c
    return True
    
def make_tidy(s):
    while s[0] == '0':
        s = s[1:]
    last_c = '0'
    for i, c in enumerate(s):
        if c < last_c:
            return make_tidy(s[:i-1] + chr(ord(s[i-1])-1) + "9"*(len(s)-i))
        last_c = c
    return s
    

T = int(lines[0],10)
for tt, l in enumerate(lines[1:]):
    N = l.strip()
    # make tidy
    ans = make_tidy(N)
    print ("Case #%d:" % (tt+1)), ans

        


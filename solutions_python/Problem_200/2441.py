
def getTidy(s):
    if len(s) == 1:
        return s
    
    a = s[0] + "0"*(len(s)-1)
    b = s[0]*len(s)

    if int(s) < int(b):
        return str(int(a)-1)
    else:
        return s[0] + getTidy(s[1:])


t = int(raw_input())

for i in range(t):
    s = str(raw_input())
    
    print "Case #{}: {}".format(i+1,getTidy(s))
        

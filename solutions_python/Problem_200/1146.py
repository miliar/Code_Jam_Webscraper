def helper():
    T = int(input())  
    
    s = [int(i) for i in str(T)]

    while (not tidy (s)):
        s = oneLoop(s)
    
    return int(''.join(str(i) for i in s))

def oneLoop(s):
    for i in reversed(xrange(len(s) - 1) ):
        s = move(s, i)
        # print(s)
    return s    

def move(s, i):     
    if s[i + 1] < s[i]:
        for j in range(i+1, len(s)):
            s[j] = 9
        if s[i] > 0:
            s[i] -= 1
        else:
            j = i
            while j > 0 and s[j] == 0:
                s[j] = 9
                j -= 1
            s[j] -= 1    
                
    return s
    

def tidy(s):
    s = str(int(''.join(str(i) for i in s)))
    flag = True
    for i in range(len(s) - 1):
        if (s[i] > s[i + 1]):
            return False
    return True  



    
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, helper())
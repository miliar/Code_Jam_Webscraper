import sys

sys.stdin = open('B-large.in', 'r')
sys.stdout = open('outputL.txt', 'w')

def tidy(s):
    for i in xrange(len(s)-1):
        if (int(s[i]) > int(s[i+1])):
            ns = s[0:i] + str(int(s[i])-1)
            for j in xrange(i+1,len(s)):
                ns += '9'
            ns = ns.lstrip('0')
            return tidy(ns)
        
    return s

for case in xrange(int(raw_input())):
    s = raw_input()
    print "Case #"+str(case+1)+": "+tidy(s)

sys.stdin.close()
sys.stdout.close()

        
                
            
        

    

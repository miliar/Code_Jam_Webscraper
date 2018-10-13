f = open("A-large.in")
def integer():
    s=f.readline()
    s=s.strip()
    s=int(s)
    return s

def string():
    s=f.readline()
    s=s.strip();
    return s

diff=0

notest=integer()

for i in range(notest):
    s=integer()
    switch=0
    d={}
    for p1 in range(s):
        string()
    q=integer()
    
    for p2 in range(q):
         last=string()
         d[last]=1
         if len(d.values()) == s :
             switch = switch + 1
             d={}
             d[last]=1
    
    print "Case #%d: %d" %(i+1, switch)    

             

        
    
        
    


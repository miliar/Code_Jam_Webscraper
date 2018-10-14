import sys,math

def find(f, seq):
    for i,item in enumerate(seq):
        if f == item: 
            return i
    return 9999999
  
    
def findlongest(se,q):
    longest = -1
    longest_se = ""
    for s in se:
        i = find(s,q)
        if i > longest:
            longest = i
            longest_se = s
    return longest
    
    

lines = sys.stdin.readlines()
it = iter(lines)
num = int(it.next())
for i in range(num):
    case = 1+i
    num_se = int(it.next())
    se = [it.next()[:-1] for j in range(num_se)]
    num_q = int(it.next())
    q = [it.next()[:-1] for j in range(num_q)]
    switches = 0
    while q:
        q = q[findlongest(se,q):]
        if q: switches += 1
    print "Case #"+str(case)+": "+str(switches)
        

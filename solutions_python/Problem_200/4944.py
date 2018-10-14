import fileinput
f = fileinput.input()
T = f.readline()

def Tidy (N):
    tid = list(str(N))
    #tid = tid.strip()
    
    temp = sorted(tid)
    if tid == temp:
        return True
    else:
        return False 
    return;
    
for case, line in enumerate(f):
    N = int(line)
    if Tidy(N):
        print "Case #{}: {}".format(case+1, N)
    else:
        
        while not Tidy(N):
            
            N -= 1
        print "Case #{}: {}".format(case+1, N)
        
        
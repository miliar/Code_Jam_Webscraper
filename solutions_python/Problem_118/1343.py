filename = 'C-small-attempt0'

f = open(filename + '.in')

outfile = open(filename + '.out', 'w')

def palin(n):
    
    num = str(n)
    half = len(num)/2
    if len(num) == 1: return True
    if len(num) % 2== 0:
        return num[:half] == num[len(num):half-1:-1]
    else:
        return num[:half] == num[len(num):half:-1]
    
     

for case in xrange(int(f.readline())):
    count = 0
    A, B = map(int, f.readline().split())
    
    for n in xrange(A,B+1):
        if palin(n):
            sqrt = float(n) ** 0.5
            if int(sqrt) == sqrt:
                if palin(int(sqrt)):
                    count += 1
            
                
    
    
    outfile.write('Case #%d: %d\n' % (case+1, count))
        
            


outfile.close()
f.close()

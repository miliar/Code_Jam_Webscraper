from math import sqrt

def is_palin(arg):
    if arg==arg[::-1]:
        return True
    else:
        return False
        
        
cases = open(' C-small-attempt0.in', 'r')
output = open('output.txt', 'w')

for count in range(int(cases.readline())):
    
    line = cases.readline().split()
    A = line[0]
    B = line[1]
    N = 0
    
    for n in range(int(A),int(B)+1):
        if is_palin(str(n)):
            if sqrt(n)==int(sqrt(n)) and is_palin(str(int(sqrt(n)))):
                N += 1
    
    output.write("Case #%i: %s\n" % (count+1, N))

cases.close()
output.close()
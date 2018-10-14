import sys

def gcd(x,y) : 
    if y==0 : 
        return x;
    else:
        return gcd(y,x%y);

t = int(sys.stdin.readline())

for i in range(t):

    line = sys.stdin.readline().split();
    g = 0 
    for j in range(len(line)-2) : 
        g = gcd(g , abs(int(line[j+1])-int(line[j+2])))  
    ans = (g - int(line[1]) % g) % g    
    print "Case #" + str(i+1) + ":" , ans; 

#http://docs.python.org/release/2.3.5/whatsnew/section-slices.html


def palindrone(a):
    a = str(a)
    b = a[::-1]
    return b == a

def findroot(a):
    return int(a**(0.5))    

def perfectSquarePalind(a):
    if palindrone(a): #Number is a palindrone
        if palindrone(findroot(a)): #Square root is also palindrone
            return ((findroot(a) * findroot(a)) == a)
    return False
            
def countPalindrones(a,b):
    count = 0
    for i in xrange(long(a),long(b+1)):
        if (perfectSquarePalind(i)):
            count = count + 1
    return count

def countPalindrones2(a,b):
    count = 0
    tempb = a *10000
    while(tempb < long(b)):
        for i in xrange(long(a),long(tempb)):
            if (perfectSquarePalind(i)):
                count = count + 1
        a = tempb
        tempb = a * 10000
    
    for i in xrange(long(a),long(b)):
            if (perfectSquarePalind(i)):
                count = count + 1    
            
    return count

f = open('C-small-attempt0.in', 'r')
g = open('C-small-attempt0.out','w')
T = int(f.readline()) #number of test cases
for j in range(T):
    A, B = ((f.readline()).strip()).split(" ") #Dont forget to correct for line end in main run
    A, B = [int(A), int(B)]
    print "Case #"+ str(j+1) + ": " + str(countPalindrones(A,B))
    g.write("Case #"+ str(j+1) + ": " + str(countPalindrones(A,B))+"\n")
g.close()
f.close()
        

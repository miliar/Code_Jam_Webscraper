import math

a = open(r"D:/downloads/C-small-attempt0.in", "r")

count = int(a.readline())

def isPali( x ):
    places = int(math.log(x, 10))
    for j in xrange(places/2 + 1):
        if (x/( int( math.pow( 10, places-j ) ) )) == (x % math.pow(10,j+1)):
            return x

ans=""
pairs = []
for k in xrange(1,count+1):
    tots = 0
    pair = a.readline().strip().split()
    start =  int(pair[0])
    end = int(pair[1])
    tots = 0
    for i in xrange(start, end+1):
        sqr = math.pow(i, .5)
        if math.floor(sqr) == math.ceil(sqr) and isPali(int(sqr)) and isPali(i):
            tots+=1
    ans += "Case #%d: %d\n" % (k, tots)
            
b = open(r"D:/downloads/c.out", "w")
b.write(ans.strip())
print ans.strip()
b.close()
a.close()

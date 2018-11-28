import sys

f = open('C-small-attempt0.in', 'r')
o = open('c.out', 'w')

T = int(f.readline().strip())

def rotate(L, N):
    return L[N:] + L[:N]

def is_dpt(int1,int2):
    int1 = str(int1)
    int2 = str(int2)
    if (len((int1)) == len((int2))):
        for i in range(1, len(int1)+1):
            if int1 ==rotate(int2,i):
                return True
                                      
    return False

for _t in xrange(T):
    line = f.readline().split(' ')
    A = int(line[0])
    B = int(line[1])
    res=0
    for i in range(A,B):#<A,B)
        for j in range(i+1,B+1):#<i+1,B>
            if is_dpt(i,j) == True:
                res +=1
                
    
    #s = f.readline()
    o.write("Case #{0}: {1}".format(_t+1, res))
    #print "Case #{0}: {1}".format(_t+1, res)
    o.write("\n")


f.close()
o.close()


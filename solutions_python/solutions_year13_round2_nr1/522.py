from sys import argv
import math

#f = open(sys.argv[1])
#f = open("B-large-practice.in")
f = open("A-small-attempt0.in")

cases = int(f.readline())


def process(A,N,M):
    M.sort()
    num = N
    count = 0
    #print "sort", M
    for i in xrange(N):
        a = M.pop(0)
        #print "a", a
        num -= 1
        if A > a:
            A += a
            
            #print "case1"
            
        else:
            #print "case2-3", A
            two_pow_n = 2**num
            if (two_pow_n * A - two_pow_n + 1) > a :
                count_j = 0
                for j in xrange(1, num+1):
                    two_pow_j = 2**j
                    temp_A = two_pow_j * A - two_pow_j + 1
                    if (temp_A) > a:
                        break
                count += j
                A = temp_A
                A += a
                #print "case2", A, temp_A, a    
            else:
                #delete mote
                count += 1
                #print "case3"
        #print "A", A
    return count
      
            

for i in xrange(cases):
    A,N = map(int, f.readline().split())
    M = map(int, f.readline().split())
    print "Case #%d:" % (i + 1), process(A,N,M)


f.close()

import sys
import gmpy

f= open(sys.argv[1])
cases = int(f.readline())
of = open(sys.argv[2],'w') 

for case in xrange(1, cases+1):
    A, B = [int(i) for i in f.readline().split()]
    count = 0
    for n in xrange(A, B+1):
        s = str(n)
        if s == s[::-1]:
            #palindrome
            root, a_square = gmpy.mpz(n).root(2)
            if a_square == 1:
                root_s = str(root)
                if root_s == root_s[::-1]:
                    count += 1
    of.write("Case #%s: %s\n" % (case, count))

#!/usr/bin/env python

def main():
    f = open('input.txt')
    import math

    total_T = int(f.readline())

    for T in xrange(1,total_T+1):
        #print T
        A,B = f.readline().rstrip('\n').split()
        A,B=long(A),long(B)
        #print A,B

        A_ = int(math.sqrt(A))
        A_ = A_ if A_*A_==A else A_+1
        B_ = int(math.sqrt(B))
        B_ = B_

        square_root_set = set([x for x in xrange(A_,B_+1) if check_palindrome(x)])


        candidate_set = set([x*x for x in square_root_set if check_palindrome(x*x)])
        #print len(candidate_set)

        print "Case #{}: {}".format(T, len(candidate_set))



        

def check_palindrome(long_int):
    long_string = str(long_int)
    for i in xrange(len(long_string)/2+1):
        if long_string[i]!=long_string[len(long_string)-1-i]:
            return False

    return True




if __name__ == '__main__':
    main()
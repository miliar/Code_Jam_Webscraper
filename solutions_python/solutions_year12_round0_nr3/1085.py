#!/usr/bin/python

if __name__ == "__main__":
    T = int(raw_input()) # T is the number of Test Cases
    for i in xrange(T):
        sA, sB = raw_input().split()
        A = int(sA)
        B = int(sB)
        st = set()
        for j in xrange(A, B+1):
            n = str(j)
            for splitpt in xrange(1, len(n)):
                m = n[splitpt:] + n[:splitpt]
                if n < m:
                    if A <= int(m) <= B:
                        snm = str(n) + "," + str(m)
                        st.add(snm)
        print "Case #" + str(i+1) + ": " + str(len(st))

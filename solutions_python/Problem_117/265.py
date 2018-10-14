#!/usr/bin/python

def main():
    with open("B-large.in") as f:
        T = int(f.readline().strip())

        for Tcur in range(1, T+1):
            (n, m) = [int(c) for c in f.readline().rstrip().split()]
            lawn = [ [int(c) for c in f.readline().rstrip().split()] for i in range(int(n)) ]

            print "Case #%d: %s" % (Tcur, foo(lawn, n, m))

        f.close()

def foo(M, n, m):
	return 'YES' if all( all(valid(M, n, m, i, j) for j in range(m)) for i in range(n) ) else 'NO'

def valid(M, n, m, i, j):
    return all(M[i][k] <= M[i][j] for k in range(m)) or \
           all(M[k][j] <= M[i][j] for k in range(n))

if __name__=="__main__":
    main()

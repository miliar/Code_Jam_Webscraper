import sys

def calc_comb(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in calc_comb(items[i+1:],n-1):
                yield [items[i]]+cc


readfile = "A-small-attempt1.in"
writefile = readfile + ".out"

open_read_file = open(readfile,'r')
open_write_file = open(writefile,'w')
num_cases = int(open_read_file.readline())
#case = 0
#for line in open_read_file.readlines():
# if firstline == 0:
#    firstline = 1
#    num_cases = int(line)
# else:
#    case = case + 1

for case in range(num_cases):
    [n,A,B,C,D,X0,Y0,M] = open_read_file.readline().split()
    n = int(n)
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    X0 = int(X0)
    Y0 = int(Y0)
    M = int(M)
    count = 0
    X = X0
    Y = Y0
    tree_list = [[X,Y]]
    for index in range(n-1):
        X = (A * X + B)% M 
        Y = (C * Y + D) % M
        tree_list.append([X,Y])

#    print tree_list
    comb_list = calc_comb(tree_list,3)
    for comb in comb_list:
	    x_cent = (comb[0][0] + comb[1][0] + comb [2][0])/3.0
	    y_cent = (comb[0][1] + comb[1][1] + comb [2][1])/3.0
#	    print comb
#	    print x_cent, y_cent
	    if int(x_cent) == x_cent:
		    if int(y_cent) == y_cent:
			    count = count + 1
#    print "count = ", count
    print "case = ", case
    open_write_file.write("Case #")
    open_write_file.write(str(case+1))
    open_write_file.write(": ")
    open_write_file.write(str(count))
    open_write_file.write('\n')
open_write_file.close()

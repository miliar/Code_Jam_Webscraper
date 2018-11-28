from math import *;

def solve(N,K) :
	subpow = floor(log2(K))
	number_of_sub_tables = pow(2,subpow)
	min_size_of_sub_tables = (N - (number_of_sub_tables-1)) // number_of_sub_tables
	remainder = (N - (number_of_sub_tables - 1)) % number_of_sub_tables

	if remainder == 0 :
		if min_size_of_sub_tables % 2 == 0 : 
			MIN = min_size_of_sub_tables//2-1
		else : 
			MIN = min_size_of_sub_tables//2
		MAX = min_size_of_sub_tables//2
	else :
		if K < number_of_sub_tables + remainder :
			if (min_size_of_sub_tables+1) % 2 == 1 :
				MIN = min_size_of_sub_tables//2
				MAX = min_size_of_sub_tables//2
			else :
				MIN = min_size_of_sub_tables//2
				MAX = min_size_of_sub_tables//2+1
		else :
			if min_size_of_sub_tables % 2 == 1 :
				MIN = min_size_of_sub_tables//2
				MAX = min_size_of_sub_tables//2
			else :
				MIN = min_size_of_sub_tables//2 - 1
				MAX = min_size_of_sub_tables//2

	return (MAX,MIN)


f = open("test.in","r")
l = f.readlines()
iteration = 0
l = l[1:]
for i in l :
    iteration += 1
    (n,k) = i.split()
    (max,min) = solve(int(n),int(k))

    print("Case #"+str(iteration)+": "+str(int(max))+" "+str(int(min)))

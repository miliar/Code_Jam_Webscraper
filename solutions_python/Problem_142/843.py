#!/usr/bin/python 

import sys
import copy

def RF(numbers_str):
	return [float(x) for x in numbers_str]
def DB (A,B,l):
	B.sort()
	A.sort()
	
	for k in range(l) :
		f = True
		for i in range(l-k) :
			if A[i+k] < B[i] :
				f = False
		if f == True:
			return l-k
	return 0
def BB (A,B,l):
	B.sort()
	A.sort()
	c = 0
	for k in range(l) :
		if B[k] < A[k] :
			c+=1
	return c
	
def read_s(s):
	tmp = s[0]
	tmp_count = 1
	B = []
	C = {}
	i = 1
	while i < len(s) :
		if s[i] == tmp :
			tmp_count+=1 
		else :
			B.append(tmp)
			B.append(tmp_count)
			tmp = s[i]
			tmp_count = 1
		i+=1
	return B

def sum_moves(D) :
	mx = max(D)
	mn = min(D)
	if mx == mn :
		return 0
	i = 0
	count_mn = 0
	count_mx = 0
	while i < len(D) :
		if D[i] == mx :
			mx_ind = i
			count_mx +=1
		if D[i] == mn :
			mn_ind = i
			count_mn +=1
		i+=1
	if count_mn > count_mx : 
		D[mx_ind] -=1
		return 1 + sum_moves(D)
	else :
		D[mn_ind] +=1
		return 1 + sum_moves(D)
		
	
	
def compute_A(A) :
	L = len(A[0])
	C = []
	for i in A:
		if len(i) != L :
			return -1
	j = 0
	while j < len(A[0]) :
		 C.append(A[0][j])
		 j+=2
	for i in A : 
		j = 0
		k = 0
		while j <len(A[0]) :
			if i[j] != C[k] :
				return -1
			j +=2
			k +=1
	sum_c = 0
	j = 1 
	while j < len(A[0]) :
		DD = []
		for kk in A :
			DD.append(kk[j])
		#print sum_moves(DD)
		sum_c += sum_moves(DD)
		j+=2
	return sum_c
				
			 
	
def main():
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		N = int(sys.stdin.readline().strip())
		A = []
		for j in range(N) :
			s = sys.stdin.readline()
			A.append(read_s(s))
		#print A
		res = compute_A(A) 	 
		sys.stdout.write('Case #{}: '.format(i+1))
		#print resd
		if res != -1 :
			sys.stdout.write('%d ' %res)
		else:
			sys.stdout.write('Fegla Won')
		sys.stdout.write('\n')	
        
        
        

if __name__ == '__main__':
	main()

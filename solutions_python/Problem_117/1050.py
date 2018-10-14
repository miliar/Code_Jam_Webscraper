'''
Created on 13/04/2013

@author: shb
'''

import sys
import numpy as np



def check_lawn(lawn, N, M):
	for i in range(N):
		for j in range(M):
			if not all(lawn[i, :] <= lawn[i, j]) and not all(lawn[:, j] <= lawn[i, j]):
				return False
	return True
			
if __name__ == '__main__':
	n = int(sys.stdin.readline())
	for case in range(n):
		N, M = map(int, sys.stdin.readline().split())
		height = []
		for i in range(N):
			height.append(map(int, sys.stdin.readline().split()))
		print 'Case #{}: {}'.format(case+1, 'YES' if check_lawn(np.array(height), N, M) else 'NO')
		
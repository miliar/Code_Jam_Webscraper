import sys
import bisect
import collections 

def solution(n,k):
	if k == 1:
		if n%2 == 0:
			return n/2, n/2 - 1
		else:
			return (n - 1)/2, (n - 1)/2
	k -= 1
	if n%2 == 1:
		if k%2 == 0:
			return solution((n-1)/2, k/2)
		else:
			return solution((n-1)/2, (k+1)/2)
	else:
		if k%2 == 0:
			return solution(n/2 - 1, k/2)
		else:
			return solution(n/2, (k+1)/2)

t = int(sys.stdin.readline())
for t0 in range(t):
    n, k = sys.stdin.readline().split(' ')
    n, k = int(n), int(k)
    res = solution(n,k)        
    print("Case #" + str(t0 + 1) + ': ' + str(res[0]) + ' ' + str(res[1]))




    
 
import numpy as np

def p1(K,crepes):
	res = [auxp1(K,crepes[i:]) for i in range(len(crepes)-K+1)]
	return max(res) 
	
def auxp1(K,crepes):
	#Max en prenant la crepe 0
	areas = [2*np.pi*c[1]*c[0] for c in crepes[1:]]
	areas.sort(reverse=True)
	
	c=crepes[0]
	return sum(areas[:K-1]) + np.pi*c[0]**2 + 2*np.pi*c[1]*c[0]
		
	

T = int(input())
for t in range(T):
	N,K = input().split()
	N,K = int(N), int(K)
	crepes = []
	for i in range(N):
		ri, hi = input().split()
		ri, hi = int(ri), int(hi)
		crepes.append((ri,hi))
		
	crepes.sort(reverse=True)
	
	print("Case #%d: %f"%(t+1,p1(K,crepes)))

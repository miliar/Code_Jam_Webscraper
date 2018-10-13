import sys
sys.stdin  = open("in.txt","r")
sys.stdout = open("out.txt","w")

memo = {}
def flip(s,l,r) :		
	return s[:l] + ''.join(['+' if s[i] == '-' else '-' for i in range(l,r)]) +s[r:]
def foo(s,k,i,f) :
	if s in memo : return memo[s]
	if i + k > len(s) :
		if s == "+"*len(s) :
			return f
		else:
			return float("inf")
	ans = min(foo(flip(s,i,i+k),k,i+1,f+1) , foo(s,k,i+1,f))
	memo[s] = ans
	return ans

def dash(s,k) :
	global memo
	memo = {}
	ans = foo(s,k,0,0)
	if ans == float("inf") : 
		return "IMPOSSIBLE"
	else : return ans
	
	
for t in range(int(input()))  :
		s,k = input().split()
		k = int(k)
		print("Case #",t+1,": ",dash(s,k),sep = '')

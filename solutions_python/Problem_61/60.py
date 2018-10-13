import math

def g(n,k,dic):
	if k==1:
		dic[(n,1)]=1
		return (1,dic)
	if dic.has_key((n,k)):
		return (dic[(n,k)], dic)
	ans = 0
	for i in range(1,k):
		(temp,dic) = g(k,i,dic)
		if k-i-1>n-k-1:
			continue
		temp *= math.factorial(n-k-1)
		#print "%s %s %s" %(n,k,i)
		temp /= math.factorial(k-i-1)
		temp /= math.factorial(n+i-2*k)
		ans += temp
	dic[(n,k)]=ans
	return (ans,dic)
		

def find(n,dic):
	ans = 0
	for k in range(1,n):
		(temp, dic) = g(n,k, dic)
		ans += temp
	return (ans, dic)

	
if __name__ == "__main__":
	f = open("c:\input.txt", "r")
	num = int(f.readline().strip())
	dic = {(2,1):1}
	for i in range(1,num+1):
		n = int(f.readline().strip())
		ans = 0
		(ans, dic) = find(n, dic)
		print "Case #%d: %s" %(i,ans%100003)
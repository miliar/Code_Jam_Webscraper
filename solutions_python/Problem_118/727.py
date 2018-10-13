MAX = 10000001

def is_palindrome(num):
	reverse = 0
	original = num

	while num>0:
		reverse = reverse*10 + num%10
		num/=10
	
	return reverse == original

def search(arr, x, smaller):
	low = 0
	high = len(arr)
	mid = (low+high)/2

	while low<high-1:
		if arr[mid] < x:
			low = mid
		elif arr[mid] > x:
			high = mid
		else:
			return mid
		mid = (low+high)/2		

	if arr[low]==x:
		return low
	elif arr[high] == x:
		return high

	if smaller == True:
		return low
	else: 
		return high

t = int(raw_input())
hsh = []

for i in range(1, MAX+1):
	if is_palindrome(i) and is_palindrome(i*i):
		hsh.append(i*i)
	
for T in range(t):
	(a,b) = tuple(map(int, raw_input().split()))
	l = search(hsh, a, False)
	r = search(hsh,b,True)
	#print("l:" + str(l) + ", r: " + str(r))
	print("Case #%s: %s"%(T+1, r-l+1))	

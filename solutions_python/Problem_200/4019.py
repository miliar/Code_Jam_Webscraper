def check(n):
	s = str(n)
	for i in range(1,len(s)):
		if(s[i]<s[i-1]):
			return False
	return True

def main():
	t = int(input())
	for i in range(1,t+1):
		n = int(input())
		while check(n)==False:
			n -= 1
		print ("Case #{}: {}".format(i,n))

if __name__ == '__main__':
	main()
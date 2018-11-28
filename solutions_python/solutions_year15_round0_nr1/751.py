def minFriendsRequired(n, s):
	count = 0
	ClapAud = 0
	ClapAud = int(s[0])
	
	for i in range(1, n + 1):
		count +=max(0, i - ClapAud)
		ClapAud = max(i, ClapAud)
		ClapAud += int(s[i])			
		
	return count 

def main():
	t = int(input())
	for k in range(t):
		n, s = input().split()
		print('Case #' + str(k + 1) + ':', minFriendsRequired(int(n), s))

if __name__ == '__main__':
	main()
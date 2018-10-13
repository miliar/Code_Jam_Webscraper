def check(s):
	for i in range(len(s)-1):
		if s[i] > s[i+1]:
			return False
	return True

def modify(s):
	le = len(s)
	for i in range(1,le):
		if( s[le-i] < s[le-i-1]):
			lis = list(s)
			temp = int(lis[le-i-1]) -1
			lis[le-i-1] = str(temp)
			lis[le-i:] = ['9']* (i)
			s = ''.join(lis)
			break
	if(check(s)):
		return s
	else:
		return modify(s)


for xa in range(1,int(input())+1):
     n = int(input())
     s = str(n)
     print("Case "+ " #"+ str(xa) +": ",end = "")
     print(int(modify(s)))

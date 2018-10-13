T = input()

dp = {' ':' ','a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','r':'t','s':'n','t':'w','u':'j','v':'p','y':'a','z':'q','x':'m','w':'f','q':'z'}


for t in range(T):
	s = raw_input().lower()
	l = list()
	for letter in s:
		l.append(dp[letter])
	
	print("Case #%d: %s" % (t+1,"".join(l)))
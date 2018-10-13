D = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'];
def main():	
	for case in range(int(raw_input())):
		res = []
		for char in raw_input().strip():
			if(char == ' '):res.append(char)
			else:res.append(D[ord(char)-ord('a')])
		print "Case #" + str(case+1) + ": " + "".join(res)

main()

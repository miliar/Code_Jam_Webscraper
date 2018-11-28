c = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
i = 1
f = open('googlerese.txt','r')
nc = int(f.readline())
#print (str(nc))

for line in f:
	t = ""
	for c in line:
		#print(ord(c))
		if(c==' '):
			t = t + ' '
		elif(ord(c)==10):
			t = t
		else:
			t = t + n[ord(c)-ord('a')]
	print "Case #"+str(i)+": "+t
	i = i + 1
f.close()
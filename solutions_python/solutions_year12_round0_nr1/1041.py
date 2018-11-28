#x='a'
#y=[]
#for i in range(26):
#	y.append(chr(ord(x)+i))
	
eng=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '];
goog=['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q',' '];


fi=open('A.in','r')
fo=open('A.out','w')
t=int(fi.readline())


for i in range(t):
	est=""
	gst=fi.readline()
	for e in gst:
		for j in range(len(goog)):
			if e==goog[j]:
				est=est+eng[j]
	fo.write("Case #"+str(i+1)+": "+est+"\n")


fi.close()
fo.close()

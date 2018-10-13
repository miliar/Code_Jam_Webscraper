import sys
#print sys.argv
#F=sys.argv
#print sys.agrv
t=input()
for i in range(t):
	n=input()
	while 1:
		T=str(n)
		l=list(T)
		if sorted(l)==l:
			#fp=open("small_output.txt","a")
			#fp.write(T)
			#fp.write("\n");
			#fp.close()
			#print "First number is %(first)d and second number is %(second)d" % {"first": first, "second":second}

			I=i+1
			print "Case #%(first)d: %(second)d" % {"first": I, "second":n}


			#print "Case #1: 129"
			#print "Case #%d: %d", (t,T)
			#print T
			break;
		n-=1

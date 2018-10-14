import sys
n=int(sys.stdin.readline())
for i in range(0,n):
	k=int(sys.stdin.readline())
	l=list()
	if k==1:
		l=map(int,(sys.stdin.readline()).split())
	else:
		sys.stdin.readline()
	if k==2:
                l=map(int,(sys.stdin.readline()).split())
        else:
                sys.stdin.readline()		
       	if k==3:
                l=map(int,(sys.stdin.readline()).split())
        else:
                sys.stdin.readline()
       	if k==4:
                l=map(int,(sys.stdin.readline()).split())
        else:
                sys.stdin.readline()
	m=int(sys.stdin.readline())
	t=list()
	if m==1:
                t=map(int,(sys.stdin.readline()).split())
        else:
                sys.stdin.readline()
        if m==2:
                t=map(int,(sys.stdin.readline()).split())
        else:
                sys.stdin.readline()
        if m==3:
                t=map(int,(sys.stdin.readline()).split())
        else:
                sys.stdin.readline()
        if m==4:
                t=map(int,(sys.stdin.readline()).split())
        else:
                sys.stdin.readline()

	count=0
	for j in l:
		if j in t:
			count = count + 1
			item = j
	if count==0:
		print "Case #" + str(i+1) + ": Volunteer cheated!"
	elif count==1:
		print "Case #" + str(i+1) + ": " + str(item)
	elif count>1:
		print "Case #" + str(i+1) + ": Bad magician!"	

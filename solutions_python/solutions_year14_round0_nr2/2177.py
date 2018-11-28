#!/usr/bin/python

iteration=100
out=open('B-large.out','w')
with open('B-large.in') as fi:
    n = [int(x) for x in fi.readline().split()]
    for y in range(1,n[0]+1):
    	C,F,X = [float(x) for x in fi.readline().split()]
    	cookies=0.0
    	f=2.0
    	t=0.0
    	done=False
    	while not done:
    		done=True
    		t=t+X/f
    		tB=t-X/f+C/f+X/(f+F);
   		if tB<t:
   			done=False
   			t=t+C/f-X/f
   			f=f+F
    	out.write('Case #' + str(int(y)) + ': ' + str(float(t)) + '\n')
    	#while cookies<X:
    	#	t=t+1.0
    	#	cookies=cookies+f
    	#	if cookies >= C and (X-cookies+C)/(f+F)>(X-cookies)/(f):
    	#		cookies = cookies - C
    	#		f = f + F
    	#excess=cookies-X
    	#t=t-excess/f
    	






#out=open('A-small-attempt3.out','w')
#with open('A-small-attempt3.in') as f:
#    n = [int(x) for x in f.readline().split()]
#    for y in range(1,n[0]+1):
#    		r1 = [int(x) for x in f.readline().split()]
#    		array1 = [[int(x) for x in f.readline().split()] for line in range(0,4)]
#    		r2 = [int(x) for x in f.readline().split()]
#    		array2 = [[int(x) for x in f.readline().split()] for line in range(0,4)]
#    		a=set(array1[r1[0]-1])
#    		b=set(array2[r2[0]-1])
#    		c=len(set.intersection(a,b))
#    		if c == 0:
#    			out.write('Case #' + str(y) + ': Volunteer cheated!\n')
#    		if c == 1:
#    			out.write('Case #' + str(y) + ': ' + str(set.intersection(a,b).pop()) + '\n')
#    		if c > 1:
#    			out.write('Case #' + str(y) + ': Bad magician!\n')

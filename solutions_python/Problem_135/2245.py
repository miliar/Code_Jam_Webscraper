#!/usr/bin/python
out=open('A-small-attempt3.out','w')
with open('A-small-attempt3.in') as f:
    n = [int(x) for x in f.readline().split()]
    for y in range(1,n[0]+1):
    		r1 = [int(x) for x in f.readline().split()]
    		array1 = [[int(x) for x in f.readline().split()] for line in range(0,4)]
    		r2 = [int(x) for x in f.readline().split()]
    		array2 = [[int(x) for x in f.readline().split()] for line in range(0,4)]
    		a=set(array1[r1[0]-1])
    		b=set(array2[r2[0]-1])
    		c=len(set.intersection(a,b))
    		if c == 0:
    			out.write('Case #' + str(y) + ': Volunteer cheated!\n')
    		if c == 1:
    			out.write('Case #' + str(y) + ': ' + str(set.intersection(a,b).pop()) + '\n')
    		if c > 1:
    			out.write('Case #' + str(y) + ': Bad magician!\n')

def display(n, g=0):
        display.ctr = display.ctr + 1
	if n==1:
                print "Case #"+str(display.ctr)+": "+str(g)
        if n==2:
                print "Case #"+str(display.ctr)+": Bad magician!"
        if n==3:
                print "Case #"+str(display.ctr)+": Volunteer cheated!"
                
display.ctr = 0
for t in range(input()):
	arr1,arr2 = list(), list()
	a1 = input()
	for i in range(4):
                a, b, c, d = raw_input().split()
                arr1.append([int(a), int(b), int(c), int(d)])
        a2 = input()
        for i in range(4):
                a, b, c, d = raw_input().split()
                arr2.append([int(a), int(b), int(c), int(d)])
        
        diff = set(arr1[a1-1]) & set(arr2[a2-1])
        if len(diff) == 1:
                display(1,next(iter(diff)))
        elif len(diff) == 0:
                display(3)
        else:
                display(2)
                
        
	

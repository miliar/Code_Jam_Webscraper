from math import pi

t = int( input() )

for testcase in range (1, t+1):
	
	n, k = [int(x) for x in input().split() ]
	palacinka = [tuple([int(x) for x in input().split() ] + [i]) for i in range (n)]
	#print(palacinka)
	podlapolomeru = sorted(palacinka, key = lambda x: x[0], reverse=True)
	podlaokraju = sorted(palacinka, key = lambda x: x[0]*x[1], reverse=True)
	#print (podlaokraju)
	
	odpoved = 0
	for spodna in range(0,n-k+1):
		R= podlapolomeru[spodna][0]
		H = podlapolomeru[spodna][1]
		index = podlapolomeru[spodna][2]
		povrch = 2*pi*R*H + pi*R**2
		kopa=1
		for p in podlaokraju:
			if kopa == k:
				break
			if p[0] <= R and p[2] != index:
				kopa +=1
				povrch += 2*pi*p[0]*p[1]
		if kopa == k:
			odpoved = max (odpoved, povrch)
	
	print ("Case #{0}: {1:2.7f}".format(testcase, odpoved) ) 
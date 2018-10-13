case = int(raw_input())

for x in range(1,case+1):
	vals = raw_input().split(' ')
	n = int(vals[0])
	k = int(vals[1])
	
	result = 'ON' if ((k % 2**n) == 2**n-1) else 'OFF'  
	
	print(('Case #%d: ' + result) % x)

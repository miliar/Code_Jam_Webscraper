def calc(case):      
	n, k = [int(r) for r in case.split()]		

	for i in range(n):
		#print i + 1, ":", k % 2**(i + 1) , '<', 2**(i), k % 2**(i + 1) < 2**(i)
		if(k % 2**(i + 1) < 2**i):
			return "OFF"
			
	return "ON"


	
		
		

f = open('A-large.in', 'r')
lines = f.readlines()   
f.close()
c = lines[0].split()[0]
#print c     
cases = [r.strip() for r in lines[1:]]
#print cases  
                       
of = open('output_a_large.txt', 'w')

for idx, case in enumerate(cases):
	of.write('Case #%(idx)i: %(i)s\n' % {'idx': idx + 1, 'i': calc(case)})                       
   
of.close()
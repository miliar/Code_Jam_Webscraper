num1 = 1111
num2 = 2222

f = open('/Users/jasonherald/Downloads/C-small-attempt2.in.txt', 'r')
f_lines = f.readlines()
ctr = 0

for line in f_lines:
	if (len(line) > 3):
		ctr = ctr + 1
		results = list()
		
		num1 = int(line.split(" ")[0])
		num2 = int(line.split(" ")[1])
		
		#print("Num: " + str(num1) + " : " + str(num2))
		
		for i in range(num1, num2):
			num_length = len(str(i))
			for n in reversed(range(1, num_length)):
				ls = list(str(i))
				nstr = ''.join(ls[n:num_length])
				#print('Original: ' + " : " + str(n) + " : " + str(i) + " : " + nstr + " : " + str(num_length))
				sstr = ''.join(ls[0:n])
				nn = int(nstr + sstr)
				#print('Modified: ' + str(nn))
				
				if (nn <= num2 and len(str(nn)) == len(str(i)) and i < nn):
					#print(str(i) + ' ' + str(nn))
					rx = str(i) + "-" + str(nn)
					if (rx not in results):
						results.append(rx)
		print("Case #" + str(ctr) + ": " + str(len(results)))
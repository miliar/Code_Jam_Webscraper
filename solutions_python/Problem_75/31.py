
def main():
	fin = open('B-large.in','r')
	fout = open('output.txt','w')
	
	T = int(fin.readline())
	
	for i in range(T):
		raw = fin.readline().strip().split(' ')
		
		combos = []
		cancels = []
		
		C = int(raw[0])
		for j in range(1,C+1):
			combos.append(raw[j])
			
		D = int(raw[C+1])
		for j in range(C+2,C+2+D):
			cancels.append(raw[j])
			
		invokeStr = raw[-1]
		
		result = ''
		for c in invokeStr:
			result = formCombos(result,c,combos)
			result = clearCancels(result,result[-1],cancels)
		
		print 'Case #' + str(i+1) + ': [' + ', '.join(list(result)) + ']'
		fout.write('Case #' + str(i+1) + ': [' + ', '.join(list(result)) + ']\n')
		
def formCombos(result, c, combos):
	if not result:
		return c
	
	for combo in combos:
		if (result[-1] == combo[0] and c == combo[1]) or (result[-1] == combo[1] and c == combo[0]):
			return result[:-1] + combo[2]
	
	return result + c
	
def clearCancels(result, c, cancels):
	if not result:
		return result
	
	cancelLetters = []
	
	for cancel in cancels:
		if cancel[0] == c:
			cancelLetters.append(cancel[1])
		elif cancel[1] == c:
			cancelLetters.append(cancel[0])
	
	for x in result:
		if x in cancelLetters:
			return ''
	return result

if __name__ == '__main__':
	main()

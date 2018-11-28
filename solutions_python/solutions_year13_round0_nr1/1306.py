with open('out', 'w') as result:
	with open('A-large.in', 'r') as data: 
		T = data.readline().strip()
		T = int(T)
		lines = list()
		for eachItem in range(T):
			for each in range(4):
				lines.append(data.readline().strip())

			for each in range(4):
				lines.append(lines[0][each] + lines[1][each] + lines[2][each] + lines[3][each])
			
			lines.append(lines[0][0] + lines[1][1] + lines[2][2] + lines[3][3])
			lines.append(lines[0][3] + lines[1][2] + lines[2][1] + lines[3][0])

			if 'XXXX' in lines or 'XXXT' in lines or 'XXTX' in lines or 'XTXX' in lines or 'TXXX' in lines:
				result.write('Case #' + str(eachItem+1) + ': X won\n')
				
			elif 'OOOO' in lines or 'OOOT' in lines or 'OOTO' in lines or 'OTOO' in lines or 'TOOO' in lines:
				result.write('Case #' + str(eachItem+1) + ': O won\n')
				
			elif '.' in lines[0] or '.' in lines[1] or '.' in lines[2] or '.' in lines[3]:
				result.write('Case #' + str(eachItem+1) + ': Game has not completed\n')

			else:
				result.write('Case #' + str(eachItem+1) + ': Draw\n')
			buffer = data.readline()
			lines.clear()
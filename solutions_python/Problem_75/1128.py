from magicka import magicka

name_input = raw_input('Input file: ')

entry = open(name_input, 'r').read().split('\n')
result = []
T = int(entry.pop(0))

for case in range(T):
	response = magicka(entry[case])
	result.append('Case #%d: [%s]' % ((case+1), ', '.join(response)))
	
saida = file('result.in', 'w')
saida.write('\n'.join(result))
saida.close()
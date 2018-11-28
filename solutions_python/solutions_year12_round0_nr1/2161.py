import sys
def main():
	inp = open('A-small-attempt1.in')
	out = open('output1','w')
	res = open('result')

	inpt = inp.read()
	inplines = inpt.split('\n')

	del inplines[-1]
	n = int(inplines[0])
	del inplines[0]

	resdata = res.read()
	maps = resdata.split('\n')

	codemap = {}

	del maps[-1]
	for mapping in maps:
		temp = mapping.split(' ')
		codemap[temp[0]] = temp[1]
	codemap[' '] = ' '
	j = 1	
	for line in inplines:
		out.writelines('Case #'+str(j)+': ')
		for i in range(len(line)):
			out.writelines(codemap[line[i]])
		out.writelines('\n')
		j+=1
	



if __name__ == '__main__':
	main()

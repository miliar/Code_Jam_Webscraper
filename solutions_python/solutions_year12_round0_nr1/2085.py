abc = map(chr, range(97, 123))
abcd = ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
input = open('./input', 'r')
output = open('./output', 'w')
line = input.readline()
n = int(line[:-1])
for x in range(n):
	a = input.readline()
	a = a[:-1]
	output.write('Case #'+str(x+1)+': ')
	for y in a:
		if y!=' ':
			k = abcd.index(y)
			output.write(abc[k])
		else:
			output.write(' ')
	output.write('\n')

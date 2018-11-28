dic = {
	1:range(17),
	2:[2,4,6,8,10,12,14,16],
	3:[6,9,12,15],
	4:[12,16],
}


inp = open('small.in','r')

f = open('small.out','w')

T = int(inp.readline())

for x in range(T):
	i = x+1
	x,r,c = map(int,inp.readline().split(' '))
	if r*c in dic[x]:
		f.write('Case #%d: GABRIEL\n'% i)
	else:
		f.write('Case #%d: RICHARD\n'% i)

inp.close()
f.close()

print dic

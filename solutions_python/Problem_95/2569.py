di = { 'a':'y' ,
	'b':'h' ,
	'c':'e' ,
	'd':'s' ,
	'e':'o' ,
	'f':'c' ,
	'g':'v' ,
	'h':'x' ,
	'i':'d' ,
	'j' :'u' ,
	'k' :'i' ,
	'l' :'g' ,
	'm' :'l' ,
	'n' :'b' ,
	'o' :'k' ,
	'p' :'r' ,
	'q' :'z' ,
	'r' :'t' ,
	's' :'n' ,
	't' :'w' ,
	'u' :'j' ,
	'v' :'p' ,
	'w' :'f' ,
	'x' :'m' ,
	'y' :'a' ,
	'z':'q',
	' ': ' ' }

fo = open('A-small-attempt0.in', 'rb')
fi = open('res.txt', 'wb')

case = fo.next()
res = ''
i = 0

while(i < case):
	inp = fo.next()
	for let in inp:
		try:
			res = res + di[let]
		except KeyError:
			continue
	fi.write('Case #' + str((i+1)) + ': ' + res + '\n')
	res = ''
	i = i+1

fo.close()
fi.close()
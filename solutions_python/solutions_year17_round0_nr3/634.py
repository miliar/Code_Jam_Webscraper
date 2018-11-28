
#inp = open("input.in", "r")
#inp = open("C-small-2-attempt0.in", "r")
inp = open("C-large.in", "r")

#outp = open("output.out", "w")
#outp = open("C-small-2-attempt0.out", "w")
outp = open("C-large.out", "w")

T = int(inp.readline().rstrip())
for i in range(T):

	n, k = map(int, inp.readline().rstrip().split())
	
	lista = [n]
	dic = {n: 1}

	while True:
		m = max(lista)
		augi = dic[m]
		dic.pop(m)
		if k <= augi:
			m -= 1
			break

		k -= augi
		lista.remove(m)
		m -= 1
		right = m - m/2
		left = m/2

		if right == left:
			if right in dic:
				dic[right] += augi*2
			else:
				dic[right] = augi*2
			if right not in lista:
				lista.append(right)
		else:
			if right in dic:
				dic[right] += augi
			else:
				dic[right] = augi
			if left in dic:
				dic[left] += augi
			else:
				dic[left] = augi
			if right not in lista:
				lista.append(right)
			if left not in lista:
				lista.append(left)

	outp.write('Case #%s: %s %s\n' %(str(i+1), str(m - m/2), str(m/2)))

inp.close()
outp.close()
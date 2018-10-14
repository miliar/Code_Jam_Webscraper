
file_in = open("C-large.in", "r")
file_out = open("C-large.out", "w")

T = int(file_in.readline().rstrip())
for i in range(T):

	n, k = map(int, file_in.readline().rstrip().split())
	
	lista = [n]
	dic = {n: 1}

	while True:
		m = max(lista)
		lala = dic[m]
		dic.pop(m)
		if k <= lala:
			m -= 1
			break

		k -= lala
		lista.remove(m)
		m -= 1
		right = m - m/2
		left = m/2

		if right == left:
			if right in dic:
				dic[right] += lala*2
			else:
				dic[right] = lala*2
			if right not in lista:
				lista.append(right)
		else:
			if right in dic:
				dic[right] += lala
			else:
				dic[right] = lala
			if left in dic:
				dic[left] += lala
			else:
				dic[left] = lala
			if right not in lista:
				lista.append(right)
			if left not in lista:
				lista.append(left)

	file_out.write('Case #%s: %s %s\n' %(str(i+1), str(m - m/2), str(m/2)))

file_in.close()
file_out.close()
# -*- coding: utf-8 -*-
N = 0
P = []

def calc():
	base = 0
	for i in P:
		q = i[1] - i[0]
		base += q*(q+1)//2 * i[2]
	P.sort()
	i = -1
	while 1:
		i+=1
		d = P[i]
		k = i
		while 1:
			k+=1
			if (k + 1 > len(P)):
				break
			j = P[k]
			if (d[1] >= j[0]) and (d[1] < j[1]):
				b = d[1]
				P[i][1] = j[1]
				P[k][1] = b
				if d[2] > j[2]:
					P.insert(i+1, [d[0], j[1], d[2] - j[2]])
					P[i][2] = j[2]
				elif d[2] < j[2]:
					o = j[2]
					P[k][2] = d[2]
					P.insert(k+1, [j[0], d[1], o - d[2]])
		if i + 1 >= len(P):
			break
	res = 0
	for i in P:
		q = i[1] - i[0]
		res += q*(q+1)//2 * i[2]
	return res - base


if __name__ == "__main__":
    s = open("A-small-attempt4.in.txt", "r")
    f = open("outputA.txt", "w")
    for i in range(int(s.readline())):
    	N, M = s.readline().split(' ')
    	N = int(N)
    	M = int(M)
    	P = []
    	for j in range(M):
    		P.append(list(map(int, s.readline().split())))
    	res = calc()
    	print(res)
    	print ('Case #{0}: {1}'.format(i+1, res),file=f)
    f.close()

import sys
import math

def tipo(cadena):
	return cadena[0:1]

def numero(cadena):
	return int(cadena[1:])

def mover_i(sec, idx, n):
	while(True):
		if idx >= n-1:
			return -1
		else:
			idx = idx + 1
			if tipo(sec[idx]) == "O":
				return idx

def mover_j(sec, idx, n):
	while(True):
		if idx >= n-1:
			return -1
		else:
			idx = idx + 1
			if tipo(sec[idx]) == "B":
				return idx

def solve(n, sec):
	t = 0
	t_total = 0
	Po = 1
	Pb = 1
	
	i_idx = mover_i(sec, -1, n)
	j_idx = mover_j(sec, -1, n)
	i = numero(sec[i_idx])
	j = numero(sec[j_idx])
	
	for idx in range(0, n):
		k = numero(sec[idx])
		tipo_k = tipo(sec[idx])
		
		if tipo_k == 'O':
			t = abs(k - Po) + 1
			Po = k
			
			if j_idx > -1:
				if Pb < j:
					Pb = Pb + t
					if Pb > j:
						Pb = j
				else:
					Pb = Pb - t
					if Pb <= j:
						Pb = j
				
				i_idx = mover_i(sec, i_idx, n)
				i = numero(sec[i_idx])
		else:
			t = abs(k - Pb) + 1
			Pb = k
			
			if i_idx > -1:
				if Po < i:
					Po = Po + t
					if Po > i:
						Po = i
				else:
					Po = Po - t
					if Po <= i:
						Po = i
					
				j_idx = mover_j(sec, j_idx, n)
				j = numero(sec[j_idx])
		
		t_total = t_total + t
	
	return t_total

def main():
	N = int(sys.stdin.readline()) + 1
	i = 0
	buf = []
	
	for i in range(1, N):
		buf = sys.stdin.readline().split()
		n = int(buf[0])
		sec = []
		del buf[0]
		
		for j in range(0, n):
			sec.append(buf[j*2] + buf[j*2 + 1])
		
		res = solve(n, sec)
		print "Case #%i: %s" % (i, res)

if __name__ == "__main__":
	main()

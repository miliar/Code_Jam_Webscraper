#-*- coding: utf-8 -*-

def solve(f):
	n = 0 # timides
	t = 0 # total em pé somado com os amigos
	friends = 0 # amigos para chamar

	for c in f:
		if c > 0 and t < n and n > 0:
			friends += n -t
			t += friends # inclui os amigos pra participar da paçoca

		t += c # independende do numero de gente em pé inclui eles :D
		n += 1 # aumentou o nivel de timides


	return friends


def main():
	T = int(raw_input())
	case = 0

	while case < T:
		case += 1

		line = raw_input()
		kV = line.split(" ")

		result = solve([int(x) for x in kV[1]])

		print "Case #%d: %s" % (case, result)

main()
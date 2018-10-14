import sys

first_line = sys.stdin.readline()


casos = int(first_line)

for i in range(1,casos+1):

	first_line = sys.stdin.readline()
	first_line = first_line.split(' ')
	D = int(first_line[0])
	N = int(first_line[1])

	menor = -1

	for j in range(0,N):


		first_line1 = sys.stdin.readline()
		first_line1 = first_line1.split(' ')
		K = float(first_line1[0])
		S = float(first_line1[1])
		tiempo = (D-K)/S

		if tiempo > menor:
			menor = tiempo

	v_annie = D/menor
	fannie = "{:10.6f}".format(v_annie)

	salida = "Case #" + str(i) + ': ' + fannie
	print salida


import numpy as np

T = int(input())

for t in range(T):

	N, R, O, Y, G, B, V = list(map(int, input().split()))

	res = ''

	impossible = False

	while (R+Y+B) > 0:
		f_R = float(R) / float(N)
		f_Y = float(Y) / float(N)
		f_B = float(B) / float(N)

		if len(res) > 0:
			f_R *= not (res[-1] == 'R')
			f_Y *= not (res[-1] == 'Y')
			f_B *= not (res[-1] == 'B')

		if f_R == 0.0 and f_Y == 0.0 and f_B == 0.0:
			impossible = True
			break

		idx = np.argmax([f_R, f_Y, f_B])

		if idx == 0:
			if R == 0:
				impossible = True
				break
			res += 'R'
			R -= 1
		elif idx == 1:
			if Y == 0:
				impossible = True
				break
			res += 'Y'
			Y -= 1
		else:
			if B == 0:
				impossible = True
				break
			res += 'B'
			B -= 1


	if len(res) > 1 and res[0] == res[-1]:
		#print("#############################")
		#
		for j in range(len(res)-1):
			a = list(res)
			temp = a[-1]
			a[-1] = a[-(j+1)]
			a[-(j+1)] = temp
			res_2 = ''.join(a)
			impossible_2 = False

			if res_2[0] == res_2[-1]:
				impossible_2 == True

			for i in range(len(res)-1):
				if res_2[i] == res_2[i+1]:
					#print("#############################")
					impossible_2 = True
			if impossible_2 == False:
				res = res_2
				impossible = False
			else:
				impossible = True

	for i in range(len(res)-1):
		if res[i] == res[i+1]:
			#print("#############################")
			impossible = False

	if impossible:
		print("Case #{}: {}".format(t+1, 'IMPOSSIBLE'))
	else:
		print("Case #{}: {}".format(t+1, res))

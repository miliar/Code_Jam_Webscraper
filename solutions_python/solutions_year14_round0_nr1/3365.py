import sys

def main():
	f = open(sys.argv[1])
	fa = open('result_gcj2014_qr1.txt', 'w')
	n = int(f.readline())

	for i in range(n):
		m1 = []
		m2 = []
		a1 = int(f.readline())
		for j in range(4):
			m1.append([int(a) for a in f.readline().split()])

		a2 = int(f.readline())
		for j in range(4):
			m2.append([int(a) for a in f.readline().split()])

		inter = list(set(m1[a1-1]).intersection(set(m2[a2-1])))

		if len(inter) == 1:
			fa.write('Case #'+str(i+1)+': '+str(inter[0])+'\n')

		elif len(inter) > 1:
			fa.write('Case #'+str(i+1)+': '+'Bad magician!'+'\n')

		elif len(inter) == 0:
			fa.write('Case #'+str(i+1)+': '+'Volunteer cheated!'+'\n')


	f.close()
	fa.close()


if __name__ == '__main__':
	main()





with open('B-large.in', 'rb') as fin, open('out.txt', 'wb') as fout:
    n = int(fin.readline().strip())

    for case in range(1, n + 1):
		num = fin.readline().strip()[::-1]

		while True:
			i = 1
			while i < len(num) and num[i - 1] >= num[i]:
				i += 1

			if i != len(num):
				num = '9' * i + chr(ord(num[i]) - 1) + num[i + 1:]
			else:

				fout.write('Case #{}: {}\n'.format(case, num[::-1].lstrip('0')))
				break
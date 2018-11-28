# -*- coding: utf-8 -*-

with open('input.txt') as f:
	with open('output.txt', 'w') as fout:
		n = int(f.readline())
		for i in range(n):
				ans = 0
				t,s,p, *mas = map(int, f.readline().split())
				for x in mas:
					if x < p:
						continue
					if x >= 3 * p:
						ans += 1
					else:
						x = x - p
						if x % 2 == 0:
							if x / 2 == p-1:
								ans +=1
							elif x / 2 == p-2 and s> 0 :
								ans +=1
								s -= 1
						else:
							if x == (p-1)+(p-2) and s > 0:
								ans +=1
								s -=1
							elif x == p+(p-1):
								ans += 1
				fout.write('Case #{0}: {1} \n'.format(i+1, ans))


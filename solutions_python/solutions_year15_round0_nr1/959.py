'''
Standing Ovation 4-10-15

'''

fin = open('standing.in','r')
fout = open('standing.out','w')

T = int(fin.readline())

for caseno in range(T):
	N, people = fin.readline().split()
	N = int(N)
	people = [int(x) for x in list(people)]
	#N = len(people), which has them sorted alphabetically.

	ans = 0
	count = 0
	for i in range(N + 1):
		if count >= i:
			count += people[i]
		elif people[i] > 0:
			ans += (i - count)
			count += (i - count) + people[i]

	fout.write("Case #" + str(caseno + 1) + ": " + str(ans) + '\n')

fin.close()
fout.close()
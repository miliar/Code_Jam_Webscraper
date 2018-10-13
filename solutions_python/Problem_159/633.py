f = open('A-large.in-2.txt')
f_out = open('output.txt', 'w')

he = f.read()

date = he.split('\n')

out = ''

cases = date.pop(0)

count = 0

d_out = []

casi = 0

for index, case in enumerate(date):
	if(count % 2 == 1):
		casi +=1
		k = case.split(" ")
		j = map(int, k)
		maxdiff = 0
		diffsum = 0
		for i,u in enumerate(j):
			if(i==0):
				continue
			newdiff = j[i-1] - j[i]
			if(newdiff > maxdiff and newdiff > 0):
				maxdiff = newdiff
			if(newdiff > 0):
				diffsum += newdiff

		pensum = 0
		for i,u in enumerate(j):
			if(i == len(j)-1):
				continue
			eaten = 0
			if(u <= maxdiff):
				pensum += u
			else:
				pensum += maxdiff
		d_out.append('Case #' + str(casi)  + ': ' + str(diffsum) + " " + str(pensum) + '\n')
	count +=1

f_out.writelines(d_out)
f_out.close()
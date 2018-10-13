import collections

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

f = [i for i in open('A-small-attempt0.in')]
f[-1] +='\n'
data = [i[:-1] for i in f]
cases = []
for i in range(int(data[0])):
	data1 = data[i*10+2:i*10+6][int(data[i*10+1])-1]+' '+data[(i)*10+7:(i)*10+11][int(data[(i)*10+6])-1]
	data1 = data1.split(' ')
	count = collections.Counter(data1)
	f1=True
	k=-1
	for j in count:
		# print(count[j])
		if count[j]==2:
			if k<0:
				k = int(j)
			else:
				f1 = False
	print(f1)
	if f1==True:
		if k>0:
			cases.append('Case #'+str(i+1)+': '+str(k))
		else:
			cases.append('Case #'+str(i+1)+': Volunteer cheated!')
	else:
		cases.append('Case #'+str(i+1)+': Bad magician!')
f1 = open('output.txt','w')
[f1.write(i+'\n') for i in cases]
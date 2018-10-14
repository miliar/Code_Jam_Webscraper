test=int(input())
for tt in range(test):
	st = int(input())
	sst=''
	for i in range(4):
		tmp = str(input())
		if i+1==st:
			sst={j for j in tmp.split(' ')}
	nd = int(input())
	snd=''
	for i in range(4):
		tmp = str(input())
		if i+1==nd:
			snd={j for j in tmp.split(' ')}
	res = sst&snd
	print("Case #%d: " % (tt+1),end='')
	if len(res)==0:print('Volunteer cheated!')
	elif len(res)==1:print(list(res)[0])
	else:print('Bad magician!')



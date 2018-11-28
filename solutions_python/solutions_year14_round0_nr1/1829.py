
s = [item.rstrip('\n') for item in open('smalls.txt','r').readlines()]
list = []
rew = int(s[0])
def main(num,c,f,x):
	list = []
	i = 0
	speed = 2.0
	list.append(x/speed)
	one = True
	while one:
		speed = 2.0
		total = 0.0
		for u in range(0,i):
			total += float(c/speed)
			speed += float(f)
		total += x/speed
		list.append(total)
		if total >= list[list.index(total)-1]:
			one = False
		else:
			i+=1
	print 'Case #' + str(num) + ': ' + str(list[list.index(total)-1])

for t in range(0,rew):
	y = t+1
	main(y,float(s[y].split()[0]),float(s[y].split()[1]),float(s[y].split()[2]))

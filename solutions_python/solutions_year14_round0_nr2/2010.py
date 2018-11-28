f = open('qualify2.txt','r')

def sec_count(x,count):
	return x/count;

def farm_sec_count(c,count):
	return c/count;

t = int(f.readline())
case = 1
lines = f.readlines()
for l1 in lines:
	l1 = l1.replace('\n','')
	c,f,x = [float(e) for e in l1.split(' ')]

	count = 2
	temp_sec = 0
	total_sec = sec_count(x, count)

	while 1:		
		sec1 = farm_sec_count(c, count)
		count = count + f
		sec2 = sec_count(x, count)
		temp_sec = temp_sec + sec2 + sec1
		if total_sec < temp_sec:
			break
		else:
			total_sec = temp_sec
			temp_sec = temp_sec - sec2

	print 'Case #' + str(case) + ': ' + str(round(total_sec,7))
	case = case + 1
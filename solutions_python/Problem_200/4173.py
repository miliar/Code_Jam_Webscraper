NOMBRE = {'0': 0, '1':1, '2':2, '3':3, 
			'4':4, '5':5, '6':6, '7':7,
			'8':8, '9':9}

def is_len_possible(num):
	tmp = str(num)
	l = len(tmp)
	res = ""
	for x in xrange(l-2, 0, -1):
		#print  NOMBRE[tmp[l-1]], NOMBRE[tmp[x]], res
		if NOMBRE[tmp[l-1]] < NOMBRE[tmp[x]]:
			res += str(tmp[x])
		else:
			return int(res[::-1]) if res != "" else 0
	return int(res[::-1]) if res != "" else 0

def is_tidy(num):
	tmp = str(num)
	for i in xrange(1, len(tmp)):
		if NOMBRE[tmp[i-1]] > NOMBRE[tmp[i]]:
			return False
	return True


def compute(tmp):
	number = int(tmp)
# 	truc = is_len_possible(number)
#	if 0!= is_len_possible(number):
#		number = number - truc
 	while number > 0:

		if is_tidy(number):
			return number

		number = number - 1

n = int(raw_input())
for i in xrange(1, n+1):
	tmp = raw_input()
	print "Case #"+str(i)+": "+ str(compute(tmp))
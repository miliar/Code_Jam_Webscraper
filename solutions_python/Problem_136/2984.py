
def Time(C,F,X,k):
	t = 0.0  
	for i in range(0,k):
		t = t  + C / (2.0+i*F)
		
	t = t + X/(2+k*F)
	return (t)

def findmin(C,F,X):
	tm = 100000000000.0
	im = 0
	for i in range(0,int(X)):
		t = Time(C,F,X,i)
		# print('<>',i,t,tm)
		if t<tm:
			tm = t
			im = i
		else:
			break
	# print (im,tm)
	return (im,tm)
# print (Time(30.0, 2.0, 100.0, 3))
# print (findmin(30.0, 2.0, 100.0))

def incFindMin(C,F,X):
	# tm = X/2.0
	# im = 0.0
	t_cur = 0.
	f_cur = 2
	for i in range(0,int(X)):
		# t = Time(C,F,X,i)
		f_cur = 2. + i * F
		t_end = X/f_cur
		t_next = C/f_cur 
		t_next_end =  t_next + X/(f_cur+F)

		if t_end < t_next_end:
			return t_cur+t_end
		
		t_cur = t_cur + t_next
		# print('<>',i,t,tm)
	


# print (findmin(500.0, 4.0, 2000.0))
# 30.0 1.0 2.0
# print (incFindMin(30.0, 1.0, 2.0))
# print (incFindMin(30.0, 2.0, 100.0))
# print (incFindMin(30.50000, 3.14159, 1999.19990))
# print (incFindMin(500.0, 4.0, 2000.0))

f = open("B-large.in")
cases = int(f.readline())
for case in range(cases):
	C,F,X = [float(x) for x in f.readline().split()]
	
	print ("Case #{}: {}".format(case+1,incFindMin(C,F,X)))



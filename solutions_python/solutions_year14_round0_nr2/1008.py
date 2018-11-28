#cookie clicker
f = open('B-large.in', 'r')
#f = open('input', 'r')
read = f.readline() #of test cases
x = 0

while x<int(read):
   vals = f.readline().split()
   v = map(float,vals)

   cval = v[0]
   fval = v[1]
   xval = v[2]

   cookies = 0.0
   ttime = 0.0000000
   cpers = 2 #number of cookies produced per second


   while cookies < xval:
   	trivial_time = xval/cpers		#time it will take to win without buying a cookie farm
   	farm_time = cval/cpers			#time it will take before you can buy a cookie farm

   	predictor =  xval/(cpers + fval)

   	if ttime + trivial_time < ttime + farm_time + predictor:
   		ttime = ttime + trivial_time
   		cookies = cookies + cpers*trivial_time
   		break
   	else:
   		cookies = cookies + farm_time*cpers
   		ttime = ttime + farm_time
   		cpers = cpers + fval
   		cookies = 0
 		

   #printing
   ttime = "%.7f" % ttime 
   print 'Case #{num}: {ttime}'.format(num = x+1,ttime = ttime)
   x = x+1

f.close()
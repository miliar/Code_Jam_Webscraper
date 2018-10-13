def mintime(c,f,x):
 time=0.; cookiespeed=2.
 while (x/(cookiespeed+f))<((x-c)/cookiespeed): time+=c/cookiespeed; cookiespeed+=f
 return time+x/cookiespeed

infile=file('B-large.in','rb+'); outfile=file('B-large.out','wb+')

for casen in range(1,int(infile.readline())+1):
 outfile.write('Case #%i: %.7f\r\n'%(casen,mintime(*[float(x) for x in infile.readline().strip().split(' ')])))
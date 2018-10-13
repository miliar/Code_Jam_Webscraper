import sys
zeroones=[]
def gen01(cur):
	if len(cur)<=25:
		gen01(cur+'0')
		gen01(cur+'1')
	zeroones.append(cur)
def check(i):
	if len(i)>51:
		return
	i=int(i)
	s=str(i*i)
	if s==s[::-1]:
		print s
check('0')
check('1')
check('2')
check('3')
gen01('1')
print >>sys.stderr,len(zeroones)
lineno=0
for item in zeroones:
	check(item+item[::-1])
	check(item+item[:-1][::-1])
	check(item+'2'+item[::-1])
	lineno+=1
	if lineno%10000==0:
		print >>sys.stderr,lineno,'/',len(zeroones)
zoreones=[]
gen01('2')
print >>sys.stderr,len(zeroones)
for item in zeroones:
	check(item+item[::-1])
	check(item+item[:-1][::-1])
	check(item+'2'+item[::-1])
	lineno+=1
	if lineno%10000==0:
		print >>sys.stderr,lineno,'/',len(zeroones)*2

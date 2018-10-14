f=open("codejam/A-small-attempt0.in","r")
o=open("codejam/A-small-attempt0.out","w")
chk=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]]
count=int(f.readline())
while 1:
	lines = f.readlines(count*5)
	if not lines:
		break
	i=0
	s=""
	for line in lines:
		if i%5==0:
			s=""
		i+=1
		s+=line.replace('\n','').replace('\r','')
		if i%5==0:
			result=['']*10
			isOn=0
			for idx in xrange(0,16):
				sb=s[idx]
				for k in xrange(0,10):
					if sb=='.':
						isOn=1
						if idx in chk[k]:
							result[k]='N'
					elif sb=='O' or sb=='X':
						if idx in chk[k]:
							if result[k]=='':
								result[k]=sb
							elif result[k]!=sb:
								result[k]='N'

			bl=False
			for k in xrange(0,10):
				if result[k]=='O' or result[k]=='X':	
					bl=True
					o.write("Case #%d: %s won\n" % (int(i/5), result[k]))
					break
			if bl==False:
				if isOn:
					o.write("Case #%d: Game has not completed\n" % (int(i/5)))
				else:
					o.write("Case #%d: Draw\n" % (int(i/5)))
f.close()
o.close()

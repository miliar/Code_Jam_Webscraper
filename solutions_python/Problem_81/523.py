#~ RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
file=open('xxA-large.in','r')
CT=int(file.readline()[:-1])
for Case in range(CT):
	N=int(file.readline()[:-1])
	#~ g=['.11.','0.00','01.1','.10.']
	#~ g=['.10','0.1','10.']
	#~ for i in g:
		#~ for j in i:
			#~ print(j,end='\t')
		#~ print()
	g=list()
	for i in range(N):
		g.append(file.readline()[:-1])
	rpi=list()
	wp=list()
	for x in g:
		loss=x.count('0')
		win=x.count('1')
		wpre=win/(win+loss)
		#~ print(win,'/',(win+loss),end=',')
		wp.append(wpre)
	#~ print()
	#~ print('wp',wp)
	owp=list()
	for i in range(N):
		ng=list()
		for j in range(N):
			if(i!=j and g[j][i]!='.'):
				str=g[j][:i]+g[j][i+1:]
				ng.append(str)
		#~ print(i+1,ng)
		Owpre=0
		#~ print('(',end='')
		for x in ng:
			loss=x.count('0')
			win=x.count('1')
			Owpre+=win/(win+loss)
			#~ print(win/(win+loss),end=',')
		#~ print(')/',len(ng),'=',Owpre/len(ng))
		owp.append(Owpre/len(ng))
		#~ print()
	#~ print('owp',owp)
	oowp=list()
	for i in range(N):
		Oowpre=0
		f=0
		for j in range(N):
			if(i!=j and g[j][i]!='.'):
				Oowpre+=owp[j]
				f+=1
				#~ print(wp[j],end='+')
		#~ print('/',f,'=',Oowpre/f)
		oowp.append(Oowpre/f)
	#~ print('oowp',oowp)

	#~ RPI=list()
	print('Case #%d:'%(Case+1))
	for i in range(N):
		rpi =float((0.25 * wp[i]) + (0.50 * owp[i]) + (0.25 * oowp[i]))
		x='%.12f'%(rpi)
		y=''+x
		for i in range(len(x)):
			if(x[len(x)-i-1]=='0'):
				y=x[:len(x)-i-1]
			else:
				break;
		print(y)
		#~ RPI.append('%.12f'%(rpi))
	
#~ print(RPI)
#~ print((0.25 * 1) + (0.5 * 0.5) + (0.25 * 7 / 12))
#~ 0.3958333333333333
#~ 0.395833333333
#~ 0.395833333333
#~ 0.39583333333333
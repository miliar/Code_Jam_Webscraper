Python 2.7.2 (default, Jun 12 2011, 14:24:46) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ip='ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qz'
>>> out='our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zq'
>>> ot=open('out.txt','w')
>>> fp=open('A-small-attempt1.in')
>>> for idx in range(int(fp.readline())):
	out_txt=''
	for val in fp.readline():
		index=ip.find(val)
		if index>=0:
			out_txt=out_txt.__add__(out[index])
	ot.write('Case #%d: %s\n'%(idx+1,out_txt))

	
>>> ot.close()
>>> 

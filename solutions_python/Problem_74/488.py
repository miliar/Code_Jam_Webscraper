#! /usr/bin/python

from sys import stdin

if __name__=='__main__':
	cases=int(stdin.readline())
	for case in xrange(1,cases+1):
		data=stdin.readline().split()[1:]
		data=[(data[i],int(data[i+1])) for i in xrange(0,len(data)-1,+2)]
		time=0
		opos=1
		otime=0
		bpos=1
		btime=0
		for item in data:
			if item[0]=='O':
				time_taken=abs(opos-item[1])
				time=max(otime+time_taken,time)+1
				otime=time
				opos=item[1]
			elif item[0]=='B':
				time_taken=abs(bpos-item[1])
				time=max(btime+time_taken,time)+1
				btime=time
				bpos=item[1]
		print "Case #%d: %d"%(case,time)
		

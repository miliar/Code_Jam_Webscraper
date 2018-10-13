import sys
def main():
	f=open(sys.argv[1])
	N=int(f.readline())
	I=0
	while N:
		I+=1
		N-=1
		T=int(f.readline())
		NA,NB=f.readline().split()
		NA=int(NA)
		NB=int(NB)
		timeTable=[]
		while NA:
			NA-=1
			start,stop=f.readline().split()
			h,m=start.split(":")
			start=int(m)+60*int(h)
			h,m=stop.split(":")
			stop=int(m)+60*int(h)
			timeTable.append((start,stop,"A","B"))
		while NB:
			NB-=1
			start,stop=f.readline().split()
			h,m=start.split(":")
			start=int(m)+60*int(h)
			h,m=stop.split(":")
			stop=int(m)+60*int(h)
			timeTable.append((start,stop,"B","A"))
		a,b=emulate(timeTable,T)
		print "Case #%d: %d %d"%(I,a,b)


def emulate(timeTable,turnTime):
	"emulates a timeTable on syntax [(time_of_start,time_of_arival,from_staion,to_station),..]"
	def depart(f,t,arrvtime):
		#print "train departs from",f,"at:",acure,"and will arive at",t,"at:",arrvtime
		if stations.get(f,0)==0:
			start[f]=start.get(f,0)+1
		else:
			stations[f]-=1;
		events.append((arrvtime,0,lambda:arrive(t)))
		events.sort()
	def arrive(t):
		#rint "train arrived:",arrvtime
		stations[t]=stations.get(t,0)+1
	start={}
	stations={}
	events=[(acure,1,(lambda f=f,t=t,arrvtime=arrvtime:depart(f,t,arrvtime+turnTime))) for acure,arrvtime,f,t in timeTable]
	events.sort()
	while events:
		time,prio,func=events.pop(0)
		func()
	return start.get("A",0),start.get("B",0)
		

if __name__=="__main__":
	main()

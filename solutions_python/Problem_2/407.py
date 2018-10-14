def getcost2 (taround,schedule,ina,inb):
        to_b=0
        to_a=0
        for s in schedule:
                if s[1] == 'dep':
                        if s[2]=='b':
                                if inb==0:
                                        return -1
                                inb=inb-1
                                to_a=to_a+1
			else:
                                if ina==0:
                                        return 1
                                ina=ina-1
                                to_b=to_b+1
		# arrive
                else:
                        if s[2]=='b':
                                inb=inb+1
			else:
                                ina=ina+1
	return 0

def getcost (taround, schedule):
        btrains=0
        atrains=0
        res = getcost2(taround,schedule,0,0)
        while res != 0:
                if res>0:
                        atrains=atrains+1
                else:
                        btrains=btrains+1
		res = getcost2(taround,schedule,atrains,btrains)
        return str(atrains) + " " + str(btrains)

fd = open ("B.in", "r")
#fd = open ("input.txt", "r")

n=int(fd.readline())
for i in range (1,n+1):
        time=int(fd.readline())
        (ab,ba)=fd.readline().split(" ")
        ab=int(ab)
        ba=int(ba)
        abtimes=[]
        for j in range(0,ab):
                (dep,arr) = fd.readline().strip('\n').replace(":","").split(" ")
                abtimes.append ((int(arr)+time,'arr','b'))
                abtimes.append ((int(dep),'dep','a'))
        batimes=[]
        for j in range(0,ba):
                (dep,arr) = fd.readline().strip('\n').replace(":","").split(" ")
                batimes.append ((int(arr)+time,'arr','a'))
                batimes.append ((int(dep),'dep','b'))
	schedule = batimes+abtimes
        schedule.sort()
        print "Case #" + str(i) + ": " + getcost (time,schedule)

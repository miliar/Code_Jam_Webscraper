class time:
    def __init__(self,h,m):
        self.h=(h+m//60)%24
        self.m=m%60

    def __cmp__(self,other):
        return self.h*60+self.m - (other.h*60+other.m)

    def __add__(self,other):
        return time(self.h+other.h,self.m+other.m)

    def __repr__(self):
        return "%02d:%02d" % (self.h,self.m)

def match_no(departure,arrival_,turnaround):
    i=j=res=0
    arrival=[x+turnaround for x in arrival_ if x+turnaround>=x]
    arrival.sort()
    departure.sort()
    print arrival
    print departure
    while i<len(departure) and j<len(arrival):
        if (arrival[j]<=departure[i]):
            i+=1
            j+=1
            res+=1
        else:
            i+=1
    print res
    return res

def main():
    infile=open("input.txt","r")
    outfile=open("output.txt","w")
    tests=int(infile.readline()[:-1])
    for i in range(tests):
        departureA=[]
        departureB=[]
        arrivalB=[]
        arrivalA=[]
        turnaround=time(0,int(infile.readline()[:-1]))
        print turnaround
        [na,nb]=map(int,infile.readline()[:-1].split(" "))
        for n in range(na):
            line=infile.readline()[:-1].split(" ")
            time0=line[0].split(":")
            time1=line[1].split(":")
            departureA.append(time(int(time0[0]),int(time0[1])))
            arrivalB.append(time(int(time1[0]),int(time1[1])))
        for n in range(nb):
            line=infile.readline()[:-1].split(" ")
            time0=line[0].split(":")
            time1=line[1].split(":")
            departureB.append(time(int(time0[0]),int(time0[1])))
            arrivalA.append(time(int(time1[0]),int(time1[1])))
        na_=na-match_no(departureA,arrivalA,turnaround)
        nb_=nb-match_no(departureB,arrivalB,turnaround)
        outfile.write("Case #%d: %d %d\n" % (i+1,na_,nb_))
    outfile.close()
    infile.close()

if __name__=="__main__":
    main()

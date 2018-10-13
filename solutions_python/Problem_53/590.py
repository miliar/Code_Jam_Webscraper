import sys
class Snapper():
        def __init__(self):
                self.switch=False
                self.power=False
        def __repr__(self):
                return "(p-%s,s-%s)"%(self.power,self.switch)
def getStateByAP(N,K):
        diff=pow(long(2),N);
        if((K-diff+1)%diff==0):
                return "ON"
        else:
                return "OFF"
def getState(N,K):
        if(K%2==0):
                return "OFF"
        snappers=[]
        i=0;
        while (i<N):
                snappers.append(Snapper());
                if i==0:
                        snappers[i].power=True #1st is always powered
                i=i+1;
        #now finger snapping
        i=long(0)
        while (i<K):
                i+=1
                #print "before",snappers
                for j in range(len(snappers)):
                        if snappers[j].power==True:
                                snappers[j].switch= not snappers[j].switch
                        if (j!=0):
                                        snappers[j].power=snappers[j-1].switch and snappers[j-1].power
                                        #print "-here for j=",j,"value(j+1)=",snappers_new[j-1].power;
                                
                #snappers=snappers_new[:]
                #print "after",snappers
        if(snappers[N-1].power and snappers[N-1].switch):
                return "ON"
        else:
                return "OFF"
file_in_name="test"
if len(sys.argv)>1:
        file_in_name=sys.argv[1]
file_in=open(file_in_name)
no_cases=int(file_in.readline().strip())
cases=[]
lines=file_in.readlines()
file_in.close()
cases=[]
for line in lines:
        case= [long(x) for x in line.strip().split(" ")]
        cases.append(case)
#print cases
file_out=open("out.txt","w")
i=1
for case in cases:
    solution=getStateByAP(*case)    
    output_str="Case #%d: %s"%(i,solution)
    file_out.write(output_str+"\n")
    #if(solution != "OFF"):
    print output_str
    i+=1
file_out.close()

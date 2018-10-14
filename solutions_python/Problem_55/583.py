import sys
class Case:
        def __init__(self,R,K,N,groups):
                self.runs=R
                self.capacity=K
                self.groups_count=N
                self.groups=groups
        def __repr__(self):
                return "R=%d,K=%d,N=%d,groups=%r"%(self.runs,self.capacity,self.groups_count,self.groups)
def getMoney(coaster):
        money=long(0)
        while(coaster.runs!=0):
                groups_in=[]
                temp=coaster.capacity
                while(coaster.capacity!=0 and len(coaster.groups)>0):
                        if(coaster.capacity-coaster.groups[0]<0):
                                break;
                        else:
                                coaster.capacity-=coaster.groups[0]
                                front=coaster.groups.pop(0)
                                money+=front
                                groups_in.append(front)
                for group in groups_in:
                        coaster.groups.append(group)
                coaster.capacity=temp               
                case.runs-=1
        return money;
file_in_name="test"
if len(sys.argv)>1:
        file_in_name=sys.argv[1]
file_in=open(file_in_name)
no_cases=int(file_in.readline().strip())
cases=[]
lines=file_in.readlines()
file_in.close()
cases=[]
for index in xrange(0,len(lines),2):
        case= [long(x) for x in lines[index].strip().split(" ")]
        groups=[long(x) for x in lines[index+1].strip().split(" ")] 
        cases.append(Case(case[0],case[1],case[2],groups))
print cases
file_out=open("out.txt","w")
i=1
for case in cases:
    solution=str(getMoney(case))   
    output_str="Case #%d: %s"%(i,solution)
    file_out.write(output_str+"\n")
    #if(solution != "OFF"):
    print output_str
    i+=1
file_out.close()

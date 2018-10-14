import sys,re
class Case:
        def __init__(self,_existing,_to_be_created):
                self.existing=list(_existing)
                self.not_existing=list(_to_be_created)
                self.count=0;
        def __repr__(self):
                return "(existing:%d not existing: %d [%s][%s])\n"%(len(self.existing),len(self.not_existing),self.existing,self.not_existing)
def getCount(case):
        for not_existing in case.not_existing:
                dirs=not_existing[1:].split("/")
                case.count+=len(dirs)
                path=""
                for directory in dirs:
                       path+="/"+directory
                       pattern=re.compile("^"+path+"/|^"+path+"$")
                       found=False
                       for existing in case.existing:
                               if pattern.match(existing) is not None:
                                       found=True
                                       break;
                       if found:
                               case.count-=1
                       else:
                               case.existing.append(path)
        return case.count;
                
file_in_name="input"
if len(sys.argv)>1:
        file_in_name=sys.argv[1]
file_in=open(file_in_name)
no_cases=int(file_in.readline().strip())
cases=[]
lines=file_in.readlines()
file_in.close()
cases=[]
index = 0
while index != len(lines):
        no_in_case = [int(x) for x in lines[index].strip().split(" ")]
        index+=1
        existing=[]
        for i in range(no_in_case[0]):
                existing.append(lines[index].strip())
                index+=1
        not_existing=[]
        for i in range(no_in_case[1]):
                not_existing.append(lines[index].strip())
                index+=1
        cases.append(Case(existing,not_existing))
        #del existing
        #del not_existing
        
#print cases
file_out=open("out.txt","w")
i=1
for case in cases:
    solution=str(getCount(case))   
    output_str="Case #%d: %s"%(i,solution)
    file_out.write(output_str+"\n")
    #if(solution != "OFF"):
    print output_str
    i+=1
file_out.close()

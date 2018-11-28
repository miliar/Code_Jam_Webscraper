filename="C:/Users/ishaan/Desktop/A-small-attempt2.in"
fil=open(filename,'r')
lines=fil.readlines()
cases=lines[0][:-1]
given=[]
for i in range(1, len(lines)):
    given.append(lines[i][:-1])    
fil.close()
filenames="C:/Users/ishaan/Desktop/out2.txt"
files=open(filenames,'w')
def caltilli(arr):
    s=0
    for k in arr:
        s=s+k
    return s        
for j in range(int(cases)):
    inp=given[j][2:]
    lis=[]
    for k in inp:
        lis.append((int)(k))
    su=0
    for i in range(0,len(lis)):
        if i==0:
            su=0
        else:
            result=caltilli(lis[0:i])
            print result
            if i>su+result:
                suprev=su
                su=su+(i-(result+suprev))
    files.write("Case #")
    files.write(str(j+1))
    files.write(": ")
    files.write(str(su))
    files.write("\n")
    
files.close()


##### Code Jam
### Magician
#####

def match(a):
    print(a[0])
    print(a[1])
    inter=set(a[0]).intersection(a[1])
    if len(inter)==1:
        return str(list(inter)[0])
    elif len(inter)==0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"
          
import os
import time
def load():
    print("starting...")
    t = time.clock()
    workdir  = os.path.join("C:\\\\","Users","olaf","CodeJam2014")
    file_name = "A-small-attempt0.in"
    out_file_name = file_name.split(".")[0] + "_result." + file_name.split(".")[1]
    out = open(os.path.join(workdir, out_file_name), "w")
    file = open(os.path.join(workdir, file_name), "r")
    i=0
    arrangementNo=-1
    lineCnt=0
    for line in file.read().splitlines():
        lineCnt+=1      
        a=line.split(" ")       
        if lineCnt>1 and len(a)==1:
            #print(line)
            rowNo = int(a[0])
            arrangementNo=(arrangementNo+1)%2
            if arrangementNo==0:
                i+=1
                rows=[]
            r=1
        elif len(a)==4:    
            if r==rowNo:
                rows.append(list(map(int, a)))
                if arrangementNo==1:
                    result="Case #" + str(i)+ ": "+ match(rows) + "\n"
                    print(result )
                    out.write(result)
            r+=1
    print(time.clock() - t)
    out.close()
    file.close()
  
load()

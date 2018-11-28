count=1
grid=[]
rowlist=[]
output=[]
def magictrick(output, grid, rowlist):
    firstnum=int(rowlist[0])
    secondnum=int(rowlist[1])
    set1=set(grid[firstnum-1])
    set2=set(grid[4+secondnum-1])
    answer=(set1 & set2)
    if answer==set():
        output.append("Volunteer cheated!")
    elif len(answer) > 1:
        output.append("Bad magician!")
    else:
        answer=list(answer)
        output.append(answer[0])
    return   
f=open("trickin.txt")
testcasenum=int(f.readline().strip())
for line in f:
    if (count % 10) ==1 or (count % 10)==6:
        rowlist.append(int(line.strip()))
    else:
        grid.append(line.split())
    if (count % 10)==0:
        magictrick(output,grid,rowlist)
        rowlist=[]
        grid=[]
    count+=1
g=open("solution1.txt","w")
for x in range(0,len(output)):
    g.write("Case #"+str(x+1)+": "+str(output[x])+"\n")
f.close()
g.close()
    
    

        


        
        
    
    
            
    

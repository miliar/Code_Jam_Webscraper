f = open('fin4.in', 'r+')
open('fout4.txt', 'w').close()
n = open('fout4.txt', 'r+')
l =  int(f.readline())
stalls = []
peeps=[]
def findLSRS(state, i):
    ls = 0
    for h in range(i-1):
        if state[i-(h)-1]==".":
            ls +=1
        else:
            break
    rs = 0
    for g in range(len(state)-i-1):
        
        if state[1+i+g]==".":
            rs +=1
        else:
            break
    return [ls,rs]
    
    

for line in f:
    stalls.append(int(line.split(" ")[0]))
    peeps.append(int(line.split(" ")[1]))

def getSpace(state):
    l=0
    longest = 0
    start = 0
    startl=0
    for i in range(len(state)):
        if state[i]==".":
            l+=1
            if state[i-1]=="O":
                start = i
            if l>longest:
                longest=l
                startl=start               
        else:
            l=0
    return [startl, longest]

for c in range(len(peeps)):
    print(c)
    state = list("O"+ "".join(["." for h in range(stalls[c])]) +"O")
    for p in range(peeps[c]):
        space=getSpace(state)
        
        state[space[0]+int((space[1]+1)/2)-1]="O"
        
        if p+1 == peeps[c]:
            lsrs =findLSRS(state, space[0]+int((space[1]+1)/2)-1)
            n.write("Case #" + str(c+1)+": " + str(max(lsrs)) + " "+str(min(lsrs))+"\n")
            print(lsrs)


        
                
    
n.close()
f.close()

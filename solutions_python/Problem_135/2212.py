input = open("in.txt",'r')
output = open('out.txt','w')

def solve(first,second,choice1,choice2):
    common = list(set(first[choice1-1]) & set(second[choice2-1]))
    i = len(common)
    if i==0:
        return "Volunteer cheated!"
    elif i ==1:
        return str(common[0])
    else:
        return "Bad magician!"

first = []
second = []
case = 0
for lino,line in enumerate(input.readlines()):       
    if(lino == 0):
        continue
    if(lino%10 == 1):
        choice1 = int(line)       
        continue
    if(lino%10 == 6):
        choice2 = int(line)       
        continue
    if(lino%10 >=2 and lino%10<=5):        
        first.append(map(int,line.split()))
        continue
    if(lino%10 >=7 or lino%10==0):       
        second.append(map(int,line.split()))       
    if(lino%10 == 0):  
        case+=1        
        a = solve(first,second,choice1,choice2)             
        output.write("Case #%d:"%case + " "+a+"\n")
        first = []
        second = []
    
output.close()
    


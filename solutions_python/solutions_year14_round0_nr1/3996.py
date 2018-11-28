inp=open('A-small-attempt2.in','r')
output=open('output','w')
lines=[]
for line in inp:
    lines.append(line.split())
case_num=int(lines.pop(0)[0])

for i in range (case_num):#for every case
    checked_lines=[lines[10*i+int(lines[10*i][0])],lines[10*i+int(lines[10*i+5][0])+5]]
    result=[]
    print (checked_lines)
    for j in range (1,17):
        if str(j) in checked_lines[0] and str(j) in checked_lines[1]:
            result.append(j)
    if len(result)==1:
        output.write("case #"+str(i+1)+": "+str(result[0])+"\n")
    elif len(result)==0:
        output.write("case #"+str(i+1)+": Volunteer cheated!\n")
    else:
        output.write("case #"+str(i+1)+": Bad magician!\n")
    print (result)
output.close()
    
    
    
        



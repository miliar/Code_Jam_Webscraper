txtFile="input.txt"
txt_file = open(txtFile);

#x=int(input())
lst=[]
for line in txt_file.readlines():
    #z=input()
    a=line.strip(" ").split()
    b=[]
    for d in range(len(a)):
        b.append(int(a.pop(0)))
    #print(b)
    lst.append(b)
x=lst.pop(0).pop()
#print(lst)

index=0
#print(len(lst))
output_file = open("output.txt", "w")
case=1
while index<len(lst):
    answer=0
    magic=0
    #print("Lahiru")
    target1=lst[index][0]
    if target1<=4 and target1>=1:
        row1=target1+index
        check1=[]
        check2=[]
        for b in range(len(lst[row1])):
            check1.append(lst[row1][b])
        target2=lst[index+5][0]
        if target2<=4 and target2>=1:
            row2=index+5+target2
            for c in range(len(lst[row2])):
                check2.append(lst[row2][c])
            for d in range(len(check1)):
                num=check1.pop()
                for e in range(len(check2)):
                    if num==check2[e]:
                        answer=num
                        magic+=1
    #print(magic)
    output_file.write("Case #")
    output_file.write(str(case))
    output_file.write(": ")
    if magic==0:
        output_file.write("Volunteer cheated!")
    elif magic==1:
        output_file.write(str(answer))
    else:
        output_file.write("Bad magician!")
    output_file.write("\n")
        
    index+=10
    case+=1
    
output_file.close()

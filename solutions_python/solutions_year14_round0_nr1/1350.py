input_file=file("A-small-attempt0.in","r")
output_file=file("output.txt","w")
test=int(input_file.readline())
for t in range(1,test+1):
    choice1=int(input_file.readline())
    for i in range(1,5):
        if i==choice1:row1=map(int,input_file.readline().split())
        else:input_file.readline()
    choice2=int(input_file.readline())
    for i in range(1,5):
        if i==choice2:row2=map(int,input_file.readline().split())
        else:input_file.readline()
    ans=0
    for element in row1:
        if element in row2:
            ans+=1
            row=element
    if(ans==1):
        output_file.write("Case #%d: %d\n"%(t,row))
    elif ans==0:
        output_file.write("Case #%d: Volunteer Cheated!\n"%(t))
    else:
        output_file.write("Case #%d: Bad Magician!\n"%(t))
input_file.close()
output_file.close()

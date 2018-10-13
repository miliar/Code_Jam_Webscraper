file_input=open("aaa.in", "r")
file_output=open("output.txt", "w")

number_of_test=file_input.readline()
number_of_test=int(number_of_test[0:number_of_test.find("\n")])

for i in range(0,number_of_test):
    
    number_of_blocks=file_input.readline()
    number_of_blocks=int(number_of_blocks[0:number_of_blocks.find("\n")])
    
    naomi=file_input.readline()
    naomi=naomi[0:naomi.find("\n")].split(" ")
    
    ken=file_input.readline()
    ken=ken[0:ken.find("\n")].split(" ")
    
    for j in range(0,number_of_blocks):
        naomi[j]=float(naomi[j])
        ken[j]=float(ken[j])

    naomi.sort()
    ken.sort()

    temp_naomi=naomi[::]
    temp_ken=ken[::]

    length=len(temp_naomi)
    count=0

    while length!=0:
        for j in range(0,length):
            if temp_naomi[j]>temp_ken[0]:
                count+=1
                del temp_naomi[j]
                del temp_ken[0]
                length=len(temp_naomi)
                break
            elif j==length-1:
                length=0
                break;

    file_output.write("Case #")
    file_output.write(str(i+1))
    file_output.write(": ")
    file_output.write(str(count))
    file_output.write(" ")

    length=len(naomi)
    count=0

    while length!=0:
        if naomi[length-1]>ken[length-1]:
            count+=1;
            del naomi[length-1]
            del ken[0]
            length=len(naomi)
        else:
            del naomi[length-1]
            del ken[length-1]
            length=len(naomi)
    
    file_output.write(str(count))
    file_output.write("\n")

file_input.close()
file_output.close()

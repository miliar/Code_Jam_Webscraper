def friends(shyness):
    #shyness is a string
    standing = 0
    friends = 0
    for i in range(len(shyness)):
        if(i>standing):
            friends += 1
            standing += 1
        standing += int(shyness[i])
    return friends


#main
Input = open("A-large.in", "r")
Output = open("A_out.out", "w")
num_cases = int(Input.readline().strip())
lst = []
for i in range(num_cases):
    shy = Input.readline().strip().split(" ")[1]
    Output.write("Case #"+str(i+1)+": "+str(friends(shy))+"\n")
    
Input.close()
Output.close()

#Magicka


#get file
raw = open("D:\B-large.in")
inputstream = raw.readlines()
raw.close()
#output
output = open("D:\output-magickal.out","w")

print("There are "+str(inputstream[0])+" test cases")


for p in range(1,len(inputstream),1):
    replacements = {}
    removals = []
    invokedstring = ""
    final = ""
    pareto = inputstream[p].split(" ")

    j = 0
    for i in range(1,int(pareto[0])+1,1):
        replacements[pareto[i][0:2]]=pareto[i][2]
        replacements[pareto[i][1]+pareto[i][0]]=pareto[i][2]
        j = i
    j+=1
    for i in range(j+1,j+int(pareto[j])+1,1):
        removals.append(pareto[i])
        removals.append(pareto[i][::-1])
    invokedstring = pareto[-1]
    for j in range(0,len(invokedstring),1):
        final+=invokedstring[j]
        if(final[-2:]in replacements):
            thing = final[-2:]
            final = final[:-2]
            final+= replacements[thing]
        for k in range(0,len(final)-1,1):
            if(final[k]+final[-1] in removals):
                final = ""
                break
    if(final[-1] == "\n"):
        final = final[:-1]
    print(final)
    if final != "":
        output.write("Case #"+str(p)+": "+"["+final[0])
        for m in range(1,len(final),1):
            output.write(", "+final[m])
        output.write("]")
        output.write("\n")

    else:
        output.write("Case #"+str(p)+": []\n")


output.close()

#Candy

#get file
raw = open("D:\C-large.in")
inputstream = raw.readlines()
raw.close()
#output
output = open("D:\output-candy.out","w")

print("There are "+str(inputstream[0])+" test cases")

#just an xor.


def patsum(thing):
    total = 0
    for i in range(0,len(thing),1):
      total ^= thing[i]
    return total


def summa(thing):
    total = 0
    for i in range(0,len(thing),1):
        total+= thing[i]
    return total


for i in range(2,len(inputstream),2):
    if(inputstream[i][-1]=="\n"):
        inputstream[i] = inputstream[i][:-1]
    test = [int(x) for x in inputstream[i].split(" ")]
    solution = -1
    if(patsum(test)==0):
        test.sort()
        solution = summa(test[1:])
    else:
        solution = "NO"
    output.write("Case #"+str(i/2)+": "+str(solution)+"\n")

output.close()


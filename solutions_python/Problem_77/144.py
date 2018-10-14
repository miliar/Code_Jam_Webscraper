#GORO


#get file
raw = open("D:\D-large.in")
inputstream = raw.readlines()
raw.close()
#output
output = open("D:\output-gorol.out","w")


print("There are "+str(inputstream[0][:-1])+" test cases")

def handle(thing):
    total = 0
    data = [int(x) for x in thing.split(" ")]
    target = [int(x) for x in thing.split(" ")]
    target.sort()
    locations = [x for x in range(0,len(target),1)]
    cycles = []
    while(locations!=[]):
        cycle = []
        current = locations[0]
        while(current in locations):
            locations.remove(current)
            cycle.append(data[current])
            current = target.index(data[current])
        cycles.append(cycle)
    #last loop

    for i in range(0,len(cycles),1):
        if(len(cycles[i])==1):
            total-=1
        total+=len(cycles[i])
    print(cycles,total)
    return total

for i in range(2,len(inputstream),2):
    if(inputstream[-1] == "\n"):
        inputstream = inputstream[:-1]
    result = handle(inputstream[i])
    output.write("Case #"+str(i/2)+": "+str(result)+".000000\n")

#for line in inputstream:
    #print(line)


output.close()
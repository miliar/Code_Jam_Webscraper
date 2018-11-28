file = open("B-large.in","r")
data = [t.split(" ") for t in file.read().strip().split("\n")][1:]
file.close()
##print(data)
results = []
for line in data:
    current = []
    combine = line[1:int(line[0])+1]
    opposed = line[int(line[0])+2:int(line[0])+int(line[int(line[0])+1])+2]
    invoke = line[-1]
    for x in invoke:
        current += [x]
        if len(current) >= 2:
            for c in combine:
                if (current[-1] == c[0] and current[-2] == c[1]) or (current[-1] == c[1] and current[-2] == c[0]):
                    current = current[:-2] + [c[2]]
        for o in opposed:
            if o[0] in current and o[1] in current:
                current = []
    results.append(current)
    

##print("\n".join(["Case #"+str(x+1)+": "+str(y) for x,y in enumerate(results)]).replace("'",""))
file = open("B-large.out","w")
file.write("\n".join(["Case #"+str(x+1)+": "+str(y) for x,y in enumerate(results)]).replace("'",""))
file.close()

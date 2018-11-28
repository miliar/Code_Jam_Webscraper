def checkk(input):
    SU = 0
    needed = 0
    for shy in range(len(input)):
        if SU >= shy:
            SU += int(input[shy])
        if (SU < shy):
            SU += (shy-SU)
            SU += int(input[shy])
            needed += 1 
    return  needed

lines = [line.rstrip('\n') for line in open('A-small-attempt1.in')]
pleh = []
for line in lines[1:]:
    pleh.append(line[2:])

with open('results','w') as results:
    n = 1
    for x in pleh:
       results.write('Case #%s: %s'%(n,checkk(x))+'\n')
       n +=1

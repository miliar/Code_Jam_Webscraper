lines = [line.rstrip('\n') for line in open('input.txt')]
count = lines.pop(0)

problems = []

for num in range(0,int(count)):
    problems.append(lines[0:10])
    lines = lines[10:]

count = 0
for trick in problems:
    count += 1
    line = []
    line.append(trick[int(trick[0])].split())
    line.append(trick[int(trick[5])+5].split())
    line = line[0]+line[1]
    
    lineset = list(set(line))

    line = [int(x) for x in line]
    lineset = [int(x) for x in lineset]
    line.sort()
    lineset.sort()
    
    print "Case #"+str(count)+":",
    if(len(lineset) < len(line)-1):
        print "Bad magician!"
    elif(len(lineset) == len(line)):
        print "Volunteer cheated!"
    else:
        for i in range(0, len(line)):
            try:
                if(line[i] != lineset[i]):
                    print line[i]
                    break
            except IndexError:
                print line[i]

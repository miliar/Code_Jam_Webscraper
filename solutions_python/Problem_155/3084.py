fin = open("A-Large.in",'r')
fout = open("A-Large-output.txt",'w')
T = int(fin.readline().strip())
case = 1
for line in fin:
    line = line.split()
    m = int(line[0])
    audience = list(line[1])
    print audience
    friends = 0
    total = 0
    for i in range(len(audience)):
        if total < i:
            friends += 1
            total += 1
        total += int(audience[i])
    fout.write("Case #%d: %d\n"%(case,friends))
    print "Case #%d: %d"%(case,friends)
    case += 1
fin.close()
fout.close()
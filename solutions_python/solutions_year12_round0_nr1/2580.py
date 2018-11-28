f = open('A-small-attempt0.in', 'r')
numlines = f.readline()
googlerese =    ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q', ' ']
english =       ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
for z in range(int(numlines)):
    line = f.readline()
    line = list(line)
    newline = []
    newsentence = ''
    for y in range(len(line)):
        for x in range(27):
            if line[y] == googlerese[x]:
                newline.append(english[x])



    print "Case #" + str(z+1) + ": " + newsentence.join(newline)

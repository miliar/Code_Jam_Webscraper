input = open('A-small-attempt0.in','r')
text = input.read()
stringlist = text.split('\n')
numofcases = int(stringlist[0])
stringlist = stringlist[1:]

result = []
for i in range(numofcases):
    answer1 = int(stringlist[0])
    arrange1 = stringlist[answer1].split(' ')
    arrange1 = [int(x) for x in arrange1]
    stringlist = stringlist[5:]
    answer2 = int(stringlist[0])
    arrange2 = stringlist[answer2].split(' ')
    arrange2 = [int(x) for x in arrange2]
    mixed = list(set(arrange1) & set(arrange2))
    if len(mixed) == 1:
        result.append(str(mixed[0]))
    elif len(mixed) == 0:
        result.append('Volunteer cheated!')
    elif len(mixed) > 1:
        result.append('Bad magician!')
    stringlist = stringlist[5:]

output = open('output','w')
for i in xrange(1,len(result)+1):
    output.write('Case #%d: %s\n' % (i,result[i-1]))
output.close()

    

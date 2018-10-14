import sys

filename = sys.argv[1]
inputfile = file(filename, 'rb')
outputfile = file("a.out", 'wb')

lines = inputfile.readlines()
testcases = int(lines[0].strip())
count = 0
while count < testcases:
    answer1 = int(lines[count*10+1].strip())
    answer2 = int(lines[count*10+6].strip())

    arrange1 = lines[count*10+2:count*10+6]
    arrange2 = lines[count*10+7:count*10+11]

    cardposs1 = arrange1[answer1-1].strip().split(' ')
#    print cardposs1
    cardpossfinal = []

    cardposs2 = arrange2[answer2-1].strip().split(' ')
    for cardposs in cardposs2:
        if cardposs1.count(cardposs) > 0:
            cardpossfinal.append(cardposs)

    if len(cardpossfinal) == 0:
        outputfile.write("Case #%i: Volunteer cheated!" % (count+1) + "\r\n")
    if len(cardpossfinal) == 1:
        outputfile.write("Case #%i: %s" % (count+1, cardpossfinal[0]) + "\r\n")
    if len(cardpossfinal) > 1:
        outputfile.write("Case #%i: Bad magician!" % (count+1) + "\r\n")


#    print answer1, answer2, arrange1, arrange2
    
    count += 1

inputfile.close()
outputfile.close()

def read_words(afile):
    words = []
    for line in afile:
            words.append(line.strip())
    return words



filename = open('poop.txt' , 'r')
T = filename.readline() #num test cases
aList = read_words(filename) # array where each element is a line of text

for i in range(int(T)):
    TheLine = aList[i]
    MaxShy = int(TheLine.split()[0])
    standing = 0
    invites = 0
    standing += (int(TheLine.split()[1][0]))
    for per in range(MaxShy):
        while (standing < (per+1)):
            standing += 1
            invites += 1
        standing += (int(TheLine.split()[1][per+1]))
        
    print "Case #"+str(i+1)+": "+str(invites)
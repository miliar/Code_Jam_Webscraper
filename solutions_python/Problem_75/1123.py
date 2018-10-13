data = open('data.in', 'r')

testNum = int(data.readline())

def find(s, l):
    for i in range(len(l)):
        if l[i] == s:
            return i
    return -1

for x in range(testNum):
    testString = data.readline().split(' ')
    combine = []
    destroy = []
    
    if int(testString[0]) != 0:
        combine = list(testString[1])
        if int(testString[2]) != 0:
            destroy = list(testString[3])
    elif int(testString[1]) != 0:
        destroy = list(testString[2])
    letters = list(testString[len(testString)-1])
    answer = []
    
    for letter in letters:
        done = False
        
        if answer == []:
            answer.append(letter)
            done = True
        elif (letter in combine[0:2]):
            index = find(letter, combine)
            
            otherLetter = ''
            if index == 0:
                otherLetter = combine[1]
            elif index == 1:
                otherLetter = combine[0]
                
            if answer[-1] == otherLetter:
                answer = answer[:-1]
                answer.append(combine[2])
                done = True
                
            
        if letter in destroy and not(done):
            
            index = find(letter, destroy)
            otherLetter = ''
            
            if index == 0:
                otherLetter = destroy[1]
            elif index == 1:
                otherLetter = destroy[0]
            if otherLetter in answer:
                answer = []
                done = True
        
        if not(done):
            answer.append(letter)
           
    if answer != []:
        if answer[-1] == '\n':
            answer = answer[:-1]
        print ('Case #' + str(x+1) + ': [' + ', '.join(answer)+']')
    else:
        print ('Case #' + str(x+1) + ': []')

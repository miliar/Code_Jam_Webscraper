fileHandler = open('input.in')
lines = fileHandler.readlines()
numberCases = lines[0]
i = 1

letters =    ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

googleized = ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']

while i < len(lines):
    gooStr = lines[i]
    engStr = ''
    for j in gooStr: 
        if j != ' ' and j != "\n":
            currentLetter = googleized.index(j)
            engStr = engStr + letters[currentLetter]
        else:
            engStr = engStr + ' '
    print 'Case #' + str(i) + ': ' + engStr
    i = i +1
        

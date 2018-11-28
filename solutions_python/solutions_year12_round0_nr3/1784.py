fileHandler = open('input.in')
lines = fileHandler.readlines()
numberCases = lines[0]
i = 1

while i < len(lines):
    line = lines[i].split()

    a = int(line[0])
    b = int(line[1])

    j = a

    r = 0
    
    while j < b:
        k = 1
        while k <= len(str(j)):
            beg = str(j)[:k]
            end = str(j)[k:]
            new = end + beg

            if a <= int(j) and j < int(new) and int(new) <= b:
                r = r + 1
            k = k + 1 
        j = j + 1    

    i = i + 1
    print 'Case #' + str(i-1) + ': ' + str(r)

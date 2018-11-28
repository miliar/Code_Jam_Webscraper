numCases = raw_input()
for n in range(int(numCases)):
    s = raw_input()
    s = s.split()
    pancakes = list(s[0])
    nflips = int(s[1])
    totalFlips = 0
    
    #go through each pancake in line up to the position of last possible flip
    for pancake in range(len(pancakes)-nflips+1):
        #if the current pancake is a sad pancake
        if pancakes[pancake] == '-':
            #flip the next nflip number of pancakes
            totalFlips += 1
            for i in range(nflips):
                if pancakes[i+pancake] == '-':
                    pancakes[i+pancake] = '+'
                else:
                    pancakes[i+pancake] = '-'
    #check if last nflip pancakes are +'s
    for pancake in range(len(pancakes)-nflips, len(pancakes)):
        if pancakes[pancake] == '-':
            output = "IMPOSSIBLE"
            break
        else:
            output = totalFlips
            
    print "Case #{}: {}".format(n+1, output)
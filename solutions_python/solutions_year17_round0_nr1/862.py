def flipPancakes(n, m):

    #print n
    #print m
    flipCount = 0

    isAllHappy = False
    impossible = False

    if n.find("-") == -1:
        isAllHappy = True

    while (isAllHappy == False):
        flippedStack = ""

        k = n.find("-")
        #print k
        if (k + m) > len(n):
            impossible = True
            isAllHappy = True
        if impossible == False:
            selectedPancakes = n[k:k+m]
            #print selectedPancakes
            flippedSelectedPancakes = ""
            for e in selectedPancakes:
                if e == "-":
                    flippedSelectedPancakes = flippedSelectedPancakes + "+"
                else:
                    flippedSelectedPancakes = flippedSelectedPancakes + "-"
            #print flippedSelectedPancakes
            stackList = list(n)
            stackList[k:k+m] = flippedSelectedPancakes
            n = "".join(stackList)
            #print n



            flipCount = flipCount + 1
            #print n

            if n.find("-") == -1:
                isAllHappy = True

    #print flipCount
    #print impossible

    if impossible == True:
        return "IMPOSSIBLE"
    else:
        return str(flipCount)


f = open('pancake2017.in', 'r')
g = open('outputP', 'w')
content = f.readlines()
numOfCases = int(content[0])
iter = 0
s = ""
for n in content:
    n_list = n.split()
    #print n_list[0]
    if iter == 0:
        pass
    else:
        print "Case #"+str(iter)+": "+ str(flipPancakes (str(n_list[0]), int(n_list[1])))
        s = s + "Case #"+str(iter)+": "+ str(flipPancakes(n_list[0], int(n_list[1]))) + "\n"
    iter = iter + 1
g.write(s)
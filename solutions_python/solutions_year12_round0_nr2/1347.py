infile = open('in-dancing.txt','r')
outfile = open('out-dancing.txt','w')
n = int(infile.readline())

for ni in range(1, n+1):
    line = infile.readline().split()
    ngoog = int(line[0])
    nsurp = int(line[1])
    best = int(line[2])
    scores = line[3:]
    scores = [int(x) for x in scores]

    ans = 0

    for i in range(ngoog):
        score = scores[i]
        if(score%3 == 0):
            if(score/3 >= best):
                ans += 1
            elif(score > 3 and ((score-3)/3)+2 >= best and ((score-3)/3)+2 <= 10 and nsurp > 0):
                nsurp -= 1
                ans += 1
        if(score%3 == 1):
            if(score > 1 and ((score-1)/3)+1 >= best):
                ans += 1
        if(score%3 == 2):
            if(score > 2 and ((score-2)/3)+1 >= best):
                ans += 1
            elif(score > 2 and ((score-2)/3)+2 >= best  and ((score-2)/3)+2 <= 10 and nsurp > 0):
                nsurp -= 1
                ans += 1    

    outfile.write('Case #' + str(ni) + ": " + str(ans) + "\n")

outfile.close()
infile.close()

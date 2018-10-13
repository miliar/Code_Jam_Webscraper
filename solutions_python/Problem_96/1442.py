def run(fileName):
    #print most_googlers(2, 8, [29,20,18,18,21],5)
    #print most_googlers(1, 5, [15,13,11], 3)
    #print most_googlers(0, 8, [23,22,21], 3)
    #print most_googlers(1, 1, [8,0], 2)
    #print most_googlers(2, 8, [29,20,8,18,18,21], 6)
    f = open(fileName)
    noOfCases = int(f.readline())
    for i in range(noOfCases):
        problem_line = map(int, f.readline().split())
        print "Case #"+str(i+1)+": "+str(most_googlers(problem_line[1], problem_line[2], problem_line[3:], problem_line[0]))
    
def most_googlers(surprises, threshold, scores, scoreslen):
    result = 0
    if threshold == 0:
        return len(scores)
    elif threshold == 1:
        count_zeros = 0
        for i in range(scoreslen):
            if scores[i] == 0:
                count_zeros = count_zeros + 1
        return len(scores) - count_zeros
    automatic_accept = threshold + (2 * (threshold - 1))
    automatic_reject = threshold + (2 * (threshold - 2))
    for j in range(scoreslen):
        if scores[j] >= automatic_accept:
            result = result + 1
        elif scores[j] < automatic_accept and scores[j] >= automatic_reject and surprises > 0:
            result = result + 1
            surprises = surprises - 1
    return result
        

import math

def best_score(total, limit):
    tentative = math.floor(total / 3)
    scores = [tentative, tentative, tentative]
    if(scores[0]+scores[1]+scores[2]==total and limit==2 and total>5):
        return scores[0] + 1
    while(scores[0]+scores[1]+scores[2]<total):
        if(scores[0]-scores[1]<limit and scores[0]-scores[2]<limit and scores[0]<10):
            scores[0] = scores[0] + 1
        elif(scores[1]-scores[2]<limit and scores[1]-scores[0]<limit and scores[1]<10):
            scores[1] = scores[1] + 1
        elif(scores[2]-scores[1]<limit and scores[2]-scores[0]<limit and scores[2]<10):
            scores[2] = scores[2] + 1
        else:
            break
    return scores[0]

input = open("B-small-attempt1.in", "r")
output = open("output.txt", "w")
cases = int(input.readline())
count = 1
while(cases>0):
    scores = input.readline().split(' ')
    scores.pop(0)
    surprises = int(scores.pop(0))
    above = int(scores.pop(0))
    result = 0
    i = 0
    for score in scores:
        score = int(score)
        if(best_score(score, 1)>=above):
            result = result + 1
        elif(best_score(score, 2)>=above and surprises>0):
            result = result + 1
            surprises = surprises - 1
        i = i + 1
    output.writelines("Case #" + str(count) + ": " + str(result) + '\n')
    count = count + 1
    cases = cases - 1
input.close()
output.close()
f = open('B-small-attempt3.in')
output=open('dancingout.out', 'w')


cases = int(f.readline())
surprises = 0

def solve():
    line = f.readline().split()
    googlers = int(line[0])
    global surprises
    surprises = int(line[1])
    neededScore = int(line[2])
    scores = line[3:]

  #  print('surprises ' + str(surprises))
  #  print('needed ' + str(neededScore))
  #  print(scores)

    answer = 0

    for x in scores:
        if scoredHigh(int(x), neededScore):
            answer += 1
  #  print('answer ' + str(answer))
  #  print('\n')
    return answer

def scoredHigh(totalScore, neededScore):
    global surprises
    if totalScore < neededScore:
        return False
    
    tri = int(totalScore/3)
    
    if tri >= neededScore:
        return True

    #surprise cases
    if totalScore % 3 == 0 and surprises > 0 and neededScore - tri == 1:
        surprises -=1
        return True
    if totalScore % 3 == 1 and surprises > 0 and neededScore - tri == 2:
        surprises -= 1
        return True
    if totalScore %3 == 2 and surprises > 0 and neededScore - tri == 2:
        surprises -= 1
        return True
    
    if totalScore % 3 == 1 and neededScore - tri == 1:
        return True
    if totalScore % 3 == 2 and neededScore - tri == 1:
        return True

    return False

for x in range(cases):
    output.write('Case #' + str(x+1) + ': ' + str(solve()) + '\n')

output.close()   
#    indScores = [tri]*3

    
 #   
 #   if totalScore % 3 == 1:
 #       indScores[0] += 1
 #   if totalScore % 3 == 2:
 #       indScores[0] += 1
 #       indScores[1] += 1
        
 #   for x in indScores:
 #       if x >= neededScore:
 #           return True

 #   if totalScore %
    
    






